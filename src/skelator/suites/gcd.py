from ..test import InfiniteBugTest, Test, TestSuite
from ..negations import NegateWithNthParameter


class GcdTest(Test):
    def _output(self, value):
        return f"{value}\n"


class GcdNegateWithNthParameter(GcdTest, NegateWithNthParameter):
    ...


class GcdInfiniteBug(GcdTest, InfiniteBugTest):
    ...


test_cases_info = [
    ([1071, 1029], 21),
    ([555, 666], 111),
    ([678, 987], 3),
    ([8767, 653], 1),
    ([16777216, 512], 512),
    ([16, 4], 4),
    ([315, 831], 3),
    ([513332, 91583315], 1),
    ([112, 135], 1),
    ([310, 55], 5),
    ([0, 55], 55)
]

suites = {}

for n in range(2):
    parameter_suite = TestSuite()
    for params, correct_out in test_cases_info:
        parameter_suite.add_test(GcdNegateWithNthParameter(
            params, correct_out, n))
    suites[f"{n}th_parameter"] = parameter_suite

for params, correct_out in test_cases_info:
    parameter_suite.add_test(GcdInfiniteBug(
        params, correct_out))
suites[f"infinite"] = parameter_suite
