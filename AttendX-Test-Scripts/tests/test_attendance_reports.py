"""
Test Automation Script: Attendance Reports & Analytics Suite
Application: AttendX Student Attendance System
Author: QA Automation Team (23IT057)
Description: Automated test cases verifying attendance percentage calculation
and low-attendance defaulter alert thresholds.
"""

import os
import sys
import unittest

# Ensure parent directory is in Python path for package imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.attendx_service import AttendXService


class TestAttendanceReports(unittest.TestCase):
    """Test suite covering attendance calculation and defaulter reports in AttendX."""

    def setUp(self):
        """Seed attendance records across multiple lecture days."""
        self.service = AttendXService()
        self.course_code = "IT501"

        # Mark 4 lectures for STU101 (Present 3, Absent 1 => 75%)
        self.service.mark_attendance("STU101", self.course_code, "2026-10-10", "Present")
        self.service.mark_attendance("STU101", self.course_code, "2026-10-11", "Present")
        self.service.mark_attendance("STU101", self.course_code, "2026-10-12", "Present")
        self.service.mark_attendance("STU101", self.course_code, "2026-10-13", "Absent")

        # Mark 4 lectures for STU102 (Present 1, Absent 3 => 25%)
        self.service.mark_attendance("STU102", self.course_code, "2026-10-10", "Present")
        self.service.mark_attendance("STU102", self.course_code, "2026-10-11", "Absent")
        self.service.mark_attendance("STU102", self.course_code, "2026-10-12", "Absent")
        self.service.mark_attendance("STU102", self.course_code, "2026-10-13", "Absent")

    def test_01_calculate_attendance_percentage(self):
        """TC_REP_01: Verify percentage calculations match expected student ratios."""
        pct_stu101 = self.service.calculate_attendance_percentage("STU101", self.course_code)
        self.assertEqual(pct_stu101, 75.0)

        pct_stu102 = self.service.calculate_attendance_percentage("STU102", self.course_code)
        self.assertEqual(pct_stu102, 25.0)

    def test_02_detect_defaulter_students_below_75_percent(self):
        """TC_REP_02: Verify defaulter identification for attendance strictly below 75%."""
        defaulters = self.service.get_defaulter_list(self.course_code, threshold=75.0)
        defaulter_ids = [d["student_id"] for d in defaulters]

        # STU102 has 25% (below 75%) -> Defaulter
        self.assertIn("STU102", defaulter_ids)
        # STU101 has 75% -> Not a defaulter under strictly < 75%
        self.assertNotIn("STU101", defaulter_ids)


if __name__ == "__main__":
    unittest.main(verbosity=2)
