import unittest
from selenium import webdriver
from AdminLogin import DemoExam
from StudentLogin import StudentExam

demo_exam= unittest.TestLoader().loadTestsFromTestCase(DemoExam)
student_exam=unittest.TestLoader().loadTestsFromTestCase(StudentExam)

test_suite= unittest.TestSuite([demo_exam, student_exam])

unittest.TextTestRunner(verbosity=2).run(test_suite)