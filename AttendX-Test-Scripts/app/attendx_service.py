"""
AttendX - Student Attendance System Core Service
Provides backend logic for authentication, attendance marking,
and attendance reporting used by automation test suites.
"""

from datetime import datetime
from typing import Dict, List, Optional


class AuthenticationError(Exception):
    """Raised when authentication fails."""
    pass


class AttendanceError(Exception):
    """Raised when attendance marking or retrieval encounters an issue."""
    pass


class AttendXService:
    def __init__(self):
        # Seed test users: username -> {password, role, name}
        self.users = {
            "student_01": {"password": "Password123!", "role": "student", "name": "Aarav Patel", "student_id": "STU101"},
            "student_02": {"password": "Password456!", "role": "student", "name": "Diya Sharma", "student_id": "STU102"},
            "faculty_01": {"password": "FacultyPass789!", "role": "faculty", "name": "Dr. Ramesh Verma"},
            "admin_01": {"password": "AdminSecure999!", "role": "admin", "name": "System Admin"}
        }

        # Seed student master data
        self.students = {
            "STU101": {"name": "Aarav Patel", "semester": 5, "branch": "IT"},
            "STU102": {"name": "Diya Sharma", "semester": 5, "branch": "IT"},
            "STU103": {"name": "Rohan Mehta", "semester": 5, "branch": "IT"},
        }

        # Seed valid courses
        self.courses = ["IT501", "IT502", "IT503", "CS504"]

        # In-memory attendance records: list of dicts
        # {record_id, student_id, course_code, date, status ('Present'|'Absent'), marked_by, timestamp}
        self.attendance_records: List[Dict] = []
        self._record_counter = 1

    def login(self, username: str, password: str, role: Optional[str] = None) -> Dict:
        """
        Authenticates a user and returns an active session payload.
        """
        if not username or not password:
            raise AuthenticationError("Username and password are required.")

        user = self.users.get(username)
        if not user or user["password"] != password:
            raise AuthenticationError("Invalid username or password.")

        if role and user["role"] != role:
            raise AuthenticationError(f"User is not registered under role '{role}'.")

        return {
            "status": "SUCCESS",
            "username": username,
            "role": user["role"],
            "name": user["name"],
            "session_token": f"sess_{username}_{int(datetime.now().timestamp())}",
            "is_authenticated": True
        }

    def mark_attendance(
        self,
        student_id: str,
        course_code: str,
        date_str: str,
        status: str,
        marked_by: str = "faculty_01"
    ) -> Dict:
        """
        Marks attendance for a student on a specific date.
        Validates student existence, course, date format, valid status, and duplicate entries.
        """
        # Validate student existence
        if student_id not in self.students:
            raise AttendanceError(f"Student ID '{student_id}' does not exist.")

        # Validate course
        if course_code not in self.courses:
            raise AttendanceError(f"Invalid course code '{course_code}'.")

        # Validate date format (YYYY-MM-DD)
        try:
            parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise AttendanceError(f"Invalid date format '{date_str}'. Expected format: YYYY-MM-DD.")

        # Validate status
        normalized_status = status.capitalize()
        if normalized_status not in ["Present", "Absent"]:
            raise AttendanceError(f"Invalid status '{status}'. Must be 'Present' or 'Absent'.")

        # Prevent duplicate attendance for the same student, course, and date
        for rec in self.attendance_records:
            if (rec["student_id"] == student_id and 
                rec["course_code"] == course_code and 
                rec["date"] == date_str):
                raise AttendanceError(
                    f"Attendance already marked for student {student_id} in {course_code} on {date_str}."
                )

        record = {
            "record_id": f"REC-{self._record_counter:04d}",
            "student_id": student_id,
            "course_code": course_code,
            "date": date_str,
            "status": normalized_status,
            "marked_by": marked_by,
            "timestamp": datetime.now().isoformat()
        }
        self._record_counter += 1
        self.attendance_records.append(record)
        return record

    def batch_mark_attendance(
        self,
        entries: List[Dict],
        course_code: str,
        date_str: str,
        marked_by: str = "faculty_01"
    ) -> Dict:
        """
        Marks attendance for a batch of students.
        """
        success_list = []
        failure_list = []

        for entry in entries:
            s_id = entry.get("student_id")
            status = entry.get("status")
            try:
                rec = self.mark_attendance(s_id, course_code, date_str, status, marked_by)
                success_list.append(rec)
            except AttendanceError as err:
                failure_list.append({"student_id": s_id, "error": str(err)})

        return {
            "total_processed": len(entries),
            "successful_count": len(success_list),
            "failed_count": len(failure_list),
            "records": success_list,
            "errors": failure_list
        }

    def get_attendance(self, student_id: str, course_code: Optional[str] = None) -> List[Dict]:
        """
        Retrieves attendance history for a given student.
        """
        if student_id not in self.students:
            raise AttendanceError(f"Student ID '{student_id}' does not exist.")

        results = [r for r in self.attendance_records if r["student_id"] == student_id]
        if course_code:
            results = [r for r in results if r["course_code"] == course_code]
        return results

    def calculate_attendance_percentage(self, student_id: str, course_code: str) -> float:
        """
        Calculates the attendance percentage of a student in a specific course.
        """
        history = self.get_attendance(student_id, course_code)
        if not history:
            return 0.0

        present_count = sum(1 for r in history if r["status"] == "Present")
        return round((present_count / len(history)) * 100, 2)

    def get_defaulter_list(self, course_code: str, threshold: float = 75.0) -> List[Dict]:
        """
        Returns list of students with attendance percentage below the minimum threshold.
        """
        defaulters = []
        for s_id, s_info in self.students.items():
            pct = self.calculate_attendance_percentage(s_id, course_code)
            if pct < threshold:
                defaulters.append({
                    "student_id": s_id,
                    "student_name": s_info["name"],
                    "course_code": course_code,
                    "attendance_percentage": pct,
                    "status": "Defaulter (< 75%)"
                })
        return defaulters
