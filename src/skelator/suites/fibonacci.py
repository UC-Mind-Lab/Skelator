from ..test import InfiniteBugTest, Test, TestSuite
from ..negations import NegateWithAddNtoOutput, NegateWithNthParameter


class FibonacciTest(Test):
    def _output(self, value):
        return f"{value}\n"


class FibonacciNegateWithNthParameter(FibonacciTest, 
        NegateWithNthParameter):
    ...


class FibonacciNegateWithAddNtoOutput(FibonacciTest, 
        NegateWithAddNtoOutput):
    ...


class FibonacciInfiniteBug(FibonacciTest, InfiniteBugTest):
    ...


test_cases_info = [
    ([0], 0),
    ([1], 1),
    ([2], 1),
    ([3], 2),
    ([4], 3),
    ([5], 5),
    ([6], 8),
    ([7], 13),
    ([8], 21),
    ([9], 34),
    ([10], 55),
    ([11], 89),
    ([12], 144)
]

suites = {}

parameter_suite = TestSuite()
for params, correct_out in test_cases_info:
    parameter_suite.add_test(FibonacciNegateWithNthParameter(
        params, correct_out, 0))
suites[f"0th_parameter"] = parameter_suite

for n in [-1,1]:
    add_suite = TestSuite()
    for params, correct_out in test_cases_info:
        add_suite.add_test(FibonacciNegateWithAddNtoOutput(
            params, correct_out, n))
    suites[f"add_{n}"] = add_suite


inf_suite = TestSuite()
for params, correct_out in test_cases_info:
    inf_suite.add_test(FibonacciInfiniteBug(
        params, correct_out))
    suites[f"infinite"] = inf_suite

