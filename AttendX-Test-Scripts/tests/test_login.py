"""
Test Automation Script: Login Functionality Test Suite
Application: AttendX Student Attendance System
Author: QA Automation Team (23IT057)
Description: Automated test cases verifying authentication, role access,
and validation logic for AttendX users.
"""

import os
import sys
import unittest

# Ensure parent directory is in Python path for package imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.attendx_service import AttendXService, AuthenticationError


class TestLoginFunctionality(unittest.TestCase):
    """Test suite covering user authentication in AttendX."""

    def setUp(self):
        """Initialize a fresh instance of AttendXService before each test."""
        self.service = AttendXService()

    def test_01_valid_student_login(self):
        """TC_AUTH_01: Verify successful login with valid student credentials."""
        session = self.service.login("student_01", "Password123!", role="student")
        self.assertTrue(session["is_authenticated"])
        self.assertEqual(session["username"], "student_01")
        self.assertEqual(session["role"], "student")
        self.assertTrue(session["session_token"].startswith("sess_student_01_"))

    def test_02_valid_faculty_login(self):
        """TC_AUTH_02: Verify successful login with valid faculty credentials."""
        session = self.service.login("faculty_01", "FacultyPass789!", role="faculty")
        self.assertTrue(session["is_authenticated"])
        self.assertEqual(session["role"], "faculty")
        self.assertEqual(session["name"], "Dr. Ramesh Verma")

    def test_03_invalid_password(self):
        """TC_AUTH_03: Verify login rejection on invalid password."""
        with self.assertRaises(AuthenticationError) as context:
            self.service.login("student_01", "WrongPassword!")
        self.assertIn("Invalid username or password", str(context.exception))

    def test_04_nonexistent_user(self):
        """TC_AUTH_04: Verify login failure when username does not exist."""
        with self.assertRaises(AuthenticationError) as context:
            self.service.login("unknown_user_99", "RandomPassword!")
        self.assertIn("Invalid username or password", str(context.exception))

    def test_05_empty_username_or_password(self):
        """TC_AUTH_05: Verify validation error when username or password is blank."""
        with self.assertRaises(AuthenticationError) as context:
            self.service.login("", "Password123!")
        self.assertIn("Username and password are required", str(context.exception))

        with self.assertRaises(AuthenticationError) as context:
            self.service.login("student_01", "")
        self.assertIn("Username and password are required", str(context.exception))

    def test_06_role_mismatch_prevention(self):
        """TC_AUTH_06: Verify security check prevents students from logging in as faculty."""
        with self.assertRaises(AuthenticationError) as context:
            self.service.login("student_01", "Password123!", role="faculty")
        self.assertIn("not registered under role 'faculty'", str(context.exception))

    def test_07_valid_admin_login(self):
        """TC_AUTH_07: Verify successful login with valid administrator credentials."""
        session = self.service.login("admin_01", "AdminSecure999!", role="admin")
        self.assertTrue(session["is_authenticated"])
        self.assertEqual(session["username"], "admin_01")
        self.assertEqual(session["role"], "admin")
        self.assertEqual(session["name"], "System Admin")
        self.assertTrue(session["session_token"].startswith("sess_admin_01_"))


if __name__ == "__main__":
    unittest.main(verbosity=2)

