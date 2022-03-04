from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from search_test import SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertions_test, search_tests])


kwargs = {"output": "smoke-report"}


runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
