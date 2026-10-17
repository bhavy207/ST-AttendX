"""
AttendX Test Runner
Discovers and executes all test suites under the tests/ directory.
Produces formatted terminal output and execution statistics.
"""

import sys
import unittest


def run_all_tests():
    print("=" * 70)
    print(" AttendX Student Attendance System - Automation Test Suite")
    print(" Target: QA Version Control Migration Project (23IT057)")
    print("=" * 70)

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    print(f" Total Tests Run : {result.testsRun}")
    print(f" Passed          : {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f" Failures        : {len(result.failures)}")
    print(f" Errors          : {len(result.errors)}")
    print("=" * 70)

    if result.wasSuccessful():
        print(">> ALL AUTOMATION TESTS PASSED SUCCESSFULLY! <<")
        return 0
    else:
        print(">> SOME TESTS FAILED! <<")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
