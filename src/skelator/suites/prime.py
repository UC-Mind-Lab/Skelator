from ..test import Test, TestSuite
from ..negations import NegateWithNthParameter


class NthPrimeTest(Test):
    def _output(nth, value):
        return f"{value}\n"


class NthPrimeNegateWithNthParameter(NthPrimeTest,
        NegateWithNthParameter):
    ...

test_cases_info = [
    ([0], 0),
    ([1], 2),
    ([2], 3),
    ([3], 5),
    ([4], 7),
    ([5], 11),
    ([6], 13),
    ([7], 17),
    ([8], 19),
    ([9], 23),
    ([10], 29),
    ([11], 31),
    ([12], 37),
    ([13], 41),
    ([14], 43),
    ([15], 47),
    ([16], 53),
    ([17], 59),
    ([18], 61),
    ([19], 67),
    ([20], 71)
]

suites = {}

parameter_suite = TestSuite(links="-lm")
for params, correct_out in test_cases_info:
    parameter_suite.add_test(NthPrimeNegateWithNthParameter(
        params, correct_out, 0))
suites[f"0th_parameter"] = parameter_suite

