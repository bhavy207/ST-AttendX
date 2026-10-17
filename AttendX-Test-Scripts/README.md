# AttendX Test Automation Scripts

[![QA Automation](https://img.shields.io/badge/QA-Automation_Suite-blue.svg)](file:///c:/Users/Administrator/Desktop/23it057/AttendX-Test-Scripts)
[![Python Version](https://img.shields.io/badge/Python-3.x-brightgreen.svg)](file:///c:/Users/Administrator/Desktop/23it057/AttendX-Test-Scripts)
[![Version Control](https://img.shields.io/badge/Git-GitHub-orange.svg)](file:///c:/Users/Administrator/Desktop/23it057/AttendX-Test-Scripts)

## 1. Project Overview & Scenario
**AttendX** is a student attendance application used across university departments. Previously, a team of three QA engineers shared automation test scripts through email and USB pen drives. This informal method resulted in:
- Overwritten scripts and merge collisions.
- Untracked regression failures and lost work.
- Lack of audit trail and accountability.

To resolve these collaboration bottlenecks, all automation test assets have been consolidated under **Git** and **GitHub** version control within this centralized repository: `AttendX-Test-Scripts`.

---

## 2. Repository Structure

```text
AttendX-Test-Scripts/
├── .gitignore                      # Ignored build, cache, and IDE artifacts
├── README.md                       # Documentation of automation suites & execution
├── run_tests.py                    # Unified test runner with formatted execution summary
├── app/
│   ├── __init__.py
│   └── attendx_service.py          # AttendX core attendance & auth logic under test
└── tests/
    ├── __init__.py
    ├── test_login.py               # Test Suite 1: User authentication & access control
    ├── test_attendance_marking.py  # Test Suite 2: Daily attendance marking & validation
    └── test_attendance_reports.py  # Test Suite 3: Attendance percentage & defaulter analytics
```

---

## 3. Automation Test Scripts Description

### Suite 1: Login Functionality (`tests/test_login.py`)
Validates authentication security, role separation, and session generation.

| Test Case ID | Test Case Name | Objective / Scenario | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC_AUTH_01** | `test_01_valid_student_login` | Student logs in with valid credentials | Authentication succeeds; active session token generated |
| **TC_AUTH_02** | `test_02_valid_faculty_login` | Faculty logs in with valid credentials | Authentication succeeds with faculty role privileges |
| **TC_AUTH_03** | `test_03_invalid_password` | Login attempt with wrong password | `AuthenticationError` raised with error message |
| **TC_AUTH_04** | `test_04_nonexistent_user` | Login attempt with unknown username | Rejection with secure error message |
| **TC_AUTH_05** | `test_05_empty_username_or_password` | Blank username or password submission | Validation exception requiring both fields |
| **TC_AUTH_06** | `test_06_role_mismatch_prevention` | Student attempting faculty-role login | Access denied due to role mismatch |

---

### Suite 2: Attendance Marking (`tests/test_attendance_marking.py`)
Validates daily attendance operations, data integrity rules, and batch recording.

| Test Case ID | Test Case Name | Objective / Scenario | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC_ATT_01** | `test_01_mark_attendance_present_success` | Mark student as 'Present' for course & date | Record created with unique `record_id` |
| **TC_ATT_02** | `test_02_mark_attendance_absent_success` | Mark student as 'Absent' | Record persisted with status 'Absent' |
| **TC_ATT_03** | `test_03_prevent_duplicate_attendance_entry` | Marking attendance twice for same student & date | Rejection with `AttendanceError` (Duplicate prevented) |
| **TC_ATT_04** | `test_04_invalid_student_id` | Attendance submission for non-existent student ID | Rejection with `AttendanceError` |
| **TC_ATT_05** | `test_05_invalid_course_code` | Attendance submission for unregistered course code | Rejection with invalid course error |
| **TC_ATT_06** | `test_06_invalid_date_format` | Non-standard date format (e.g. DD-MM-YYYY) | Validation error requiring YYYY-MM-DD |
| **TC_ATT_07** | `test_07_batch_attendance_marking` | Batch marking for multiple students | All entries processed with success status |

---

### Suite 3: Reports & Analytics (`tests/test_attendance_reports.py`)
Validates attendance calculation logic and automatic defaulter (<75%) detection.

| Test Case ID | Test Case Name | Objective / Scenario | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC_REP_01** | `test_01_calculate_attendance_percentage` | Percentage computation over lecture history | Exact percentage returned (e.g., 75.0%, 25.0%) |
| **TC_REP_02** | `test_02_detect_defaulter_students_below_75_percent` | Filter students with attendance under 75% | Defaulter list correctly identifies STU102 |

---

## 4. How to Execute Tests

### Prerequisites
- Python 3.8+ installed
- Terminal / PowerShell or VS Code Integrated Terminal

### Running All Tests
From the root of the repository (`AttendX-Test-Scripts`):
```bash
python run_tests.py
```

### Running Individual Test Suites
```bash
# Run Login Tests only
python tests/test_login.py

# Run Attendance Marking Tests only
python tests/test_attendance_marking.py

# Run Reports Tests only
python tests/test_attendance_reports.py
```

---

## 5. QA Team Git Collaboration Workflow

To ensure the 3 QA engineers do not overwrite each other's work:
1. **Always Pull Before Working**: `git pull origin main` to synchronize local branch with remote.
2. **Feature Branches**: Create task branches (e.g., `git checkout -b feature/test-qr-attendance`).
3. **Descriptive Commits**: Use semantic commit messages (e.g., `feat(tests): add automated tests for attendance marking`).
4. **Code Reviews via Pull Requests**: Merge changes only after peer review on GitHub.
