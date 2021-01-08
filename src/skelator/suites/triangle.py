from ..test import InfiniteBugTest, Test, TestSuite
from ..negations import NegateBooleanOutput


class TriangleTest(Test):
    def _output(self, value):
        if value:
            return "Yes\n"
        else:
            return "No\n"


class TriangleNegateBooleanOutput(TriangleTest, NegateBooleanOutput):
    ...


class TriangleInfiniteBug(TriangleTest, InfiniteBugTest):
    ...


test_cases_info = [
    ([1, 2, 3, 1, 2, 3], False),
    ([1, 5, 2, 5, 4, 6], True),
    ([1, 1, 1, 4, 1, 5], False),
    ([1, 2, 3, 3, 2, 1], False),
    ([10, 6, 7, 3, 2, 1], True),
    ([1, 1, 2, 2, 3, 3], True)
]

suites = {}
reversed_suite = TestSuite()
for params, correct_out in test_cases_info:
    reversed_suite.add_test(TriangleNegateBooleanOutput(
        params, correct_out))
suites[f"reversed"] = reversed_suite

inf_suite = TestSuite()
for params, correct_out in test_cases_info:
    inf_suite.add_test(TriangleInfiniteBug(
        params, correct_out))
    suites[f"infinite"] = inf_suite

