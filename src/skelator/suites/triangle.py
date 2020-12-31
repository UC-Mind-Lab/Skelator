from ..test import Test, TestSuite
from ..negations import NegateBooleanOutput


class TriangleTest(Test):
    def _output(self, value):
        if value:
            return "Yes\n"
        else:
            return "No\n"


class TriangleNegateBooleanOutput(TriangleTest, NegateBooleanOutput):
    ...


test_cases_info = [
    ([1, 2, 3, 1, 2, 3], False),
    ([1, 2, 3, 3, 2, 1], True),
    ([1, 3, 3, 3, 3, 1], True),
    ([1, 1, 1, 1, 1, 1], False)
]

suites = {}
reversed_suite = TestSuite()
for params, correct_out in test_cases_info:
    reversed_suite.add_test(TriangleNegateBooleanOutput(
        params, correct_out))
suites[f"reversed"] = reversed_suite

