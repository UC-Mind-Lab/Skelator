from ..test import InfiniteBugTest, Test, TestSuite
from ..negations import NegateWithNthParameter


class LcmTest(Test):
    def _output(self, value):
        return f"{value}\n"


class LcmNegateWithNthParameter(LcmTest, NegateWithNthParameter):
    ...


class LcmInfiniteBug(LcmTest, InfiniteBugTest):
    ...


shared_test_cases_info = [
    ([1071, 1029], 52479),
    ([555, 666], 3330),
    ([678, 987], 223062),
    ([8767, 653], 5724851),
    ([16, 4], 16),
    ([315, 831], 87255),
    ([112, 135], 15120),
    ([310, 55], 3410),
    ([0, 55], 0),
    ([55, 0], 0)
]

direct_test_cases_info = [
    # It's supposed to be 47012646255580, but there is an
    # integer overflow.
    ([513332, 91583315],
        "Error: An overflow has occurred."),
    # In the other program there is an undetected overflow.
    ([16777216, 512], 16777216)
]

with_gcd_test_cases_info = [
    # It's supposed to be 47012646255580, but there is an
    # integer overflow.
    # In this case it's undetected.
    ([513332, 91583315],
        65766436),
    # It's supposed to be 16777216, but there is an
    # integer overflow.
    # In this case it's undetected.
    ([16777216, 512], 0)
]


def prepare_suite(unique_test_cases_info):
    suites = {}
    for n in range(2):
        parameter_suite = TestSuite()
        # Shared tests cases
        for params, correct_out in shared_test_cases_info:
            parameter_suite.add_test(LcmNegateWithNthParameter(
                params, correct_out, n))
        # Unique test cases
        for params, correct_out in unique_test_cases_info:
            parameter_suite.add_test(LcmNegateWithNthParameter(
                params, correct_out, n))
        # Save it
        suites[f"{n}th_parameter"] = parameter_suite

    inf_suite = TestSuite()
    for params, correct_out in unique_test_cases_info:
        inf_suite.add_test(LcmInfiniteBug(
            params, correct_out))
        suites[f"infinite"] = inf_suite

    return suites

direct_suites = prepare_suite(direct_test_cases_info)
with_gcd_suites = prepare_suite(with_gcd_test_cases_info)

