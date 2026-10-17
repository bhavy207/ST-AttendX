"""
Test Automation Script: Attendance Marking Test Suite
Application: AttendX Student Attendance System
Author: QA Automation Team (23IT057)
Description: Automated test cases verifying attendance marking, duplicate prevention,
data validation, and batch marking logic.
"""

import os
import sys
import unittest

# Ensure parent directory is in Python path for package imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.attendx_service import AttendXService, AttendanceError


class TestAttendanceMarking(unittest.TestCase):
    """Test suite covering student attendance marking operations in AttendX."""

    def setUp(self):
        """Initialize a fresh instance of AttendXService before each test."""
        self.service = AttendXService()
        self.test_date = "2026-10-17"
        self.course_code = "IT501"

    def test_01_mark_attendance_present_success(self):
        """TC_ATT_01: Verify successful marking of 'Present' attendance for a student."""
        record = self.service.mark_attendance(
            student_id="STU101",
            course_code=self.course_code,
            date_str=self.test_date,
            status="Present",
            marked_by="faculty_01"
        )
        self.assertIsNotNone(record["record_id"])
        self.assertEqual(record["student_id"], "STU101")
        self.assertEqual(record["status"], "Present")
        self.assertEqual(record["course_code"], self.course_code)
        self.assertEqual(record["date"], self.test_date)

    def test_02_mark_attendance_absent_success(self):
        """TC_ATT_02: Verify successful marking of 'Absent' status."""
        record = self.service.mark_attendance(
            student_id="STU102",
            course_code=self.course_code,
            date_str=self.test_date,
            status="Absent",
            marked_by="faculty_01"
        )
        self.assertEqual(record["status"], "Absent")
        self.assertEqual(record["student_id"], "STU102")

    def test_03_prevent_duplicate_attendance_entry(self):
        """TC_ATT_03: Verify system prevents duplicate attendance for same student/course/date."""
        # First marking succeeds
        self.service.mark_attendance(
            student_id="STU101",
            course_code=self.course_code,
            date_str=self.test_date,
            status="Present"
        )

        # Second marking on identical student, course, date must fail
        with self.assertRaises(AttendanceError) as context:
            self.service.mark_attendance(
                student_id="STU101",
                course_code=self.course_code,
                date_str=self.test_date,
                status="Present"
            )
        self.assertIn("already marked", str(context.exception))

    def test_04_invalid_student_id(self):
        """TC_ATT_04: Verify rejection when marking attendance for non-existent student ID."""
        with self.assertRaises(AttendanceError) as context:
            self.service.mark_attendance(
                student_id="STU999",
                course_code=self.course_code,
                date_str=self.test_date,
                status="Present"
            )
        self.assertIn("does not exist", str(context.exception))

    def test_05_invalid_course_code(self):
        """TC_ATT_05: Verify rejection when invalid course code is supplied."""
        with self.assertRaises(AttendanceError) as context:
            self.service.mark_attendance(
                student_id="STU101",
                course_code="INVALID999",
                date_str=self.test_date,
                status="Present"
            )
        self.assertIn("Invalid course code", str(context.exception))

    def test_06_invalid_date_format(self):
        """TC_ATT_06: Verify error handling on malformed date input string."""
        with self.assertRaises(AttendanceError) as context:
            self.service.mark_attendance(
                student_id="STU101",
                course_code=self.course_code,
                date_str="17-10-2026",  # DD-MM-YYYY instead of YYYY-MM-DD
                status="Present"
            )
        self.assertIn("Expected format: YYYY-MM-DD", str(context.exception))

    def test_07_batch_attendance_marking(self):
        """TC_ATT_07: Verify batch attendance processing for multiple students in a single call."""
        batch_entries = [
            {"student_id": "STU101", "status": "Present"},
            {"student_id": "STU102", "status": "Absent"},
            {"student_id": "STU103", "status": "Present"},
        ]
        result = self.service.batch_mark_attendance(
            entries=batch_entries,
            course_code=self.course_code,
            date_str=self.test_date,
            marked_by="faculty_01"
        )
        self.assertEqual(result["total_processed"], 3)
        self.assertEqual(result["successful_count"], 3)
        self.assertEqual(result["failed_count"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
