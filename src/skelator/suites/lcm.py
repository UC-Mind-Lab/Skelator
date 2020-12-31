from ..test import Test, TestSuite
from ..negations import NegateWithNthParameter


class LcmTest(Test):
    def _output(self, value):
        return f"{value}\n"


class LcmNegateWithNthParameter(LcmTest, NegateWithNthParameter):
    ...


test_cases_info = [
    ([1071, 1029], 52479),
    ([555, 666], 3330),
    ([678, 987], 223062),
    ([8767, 653], 5724851),
    ([16777216, 512], 16777216),
    ([16, 4], 16),
    ([315, 831], 87255),
    ([513332, 91583315],
        "Error: An overflow has occurred."),
    ([112, 135], 15120),
    ([310, 55], 3410),
    ([0, 55], 0),
    ([55, 0], 0)
]

suites = {}

for n in range(2):
    parameter_suite = TestSuite()
    for params, correct_out in test_cases_info:
        parameter_suite.add_test(LcmNegateWithNthParameter(
            params, correct_out, n))
    suites[f"{n}th_parameter"] = parameter_suite

