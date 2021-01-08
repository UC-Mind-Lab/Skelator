from ..test import InfiniteBugTest, Test, TestSuite
from ..negations import NegateWithAddNtoOutput


class ZuneTest(Test):
    def _output(self, value):
        return f"current year is {value}\n"


class ZuneNegateWithNthParamter(ZuneTest, NegateWithAddNtoOutput):
    ...


class ZuneInfiniteBug(ZuneTest, InfiniteBugTest):
    ...


test_cases_info = [
    ([10593], 2008),
    ([12054], 2012),
    ([1827], 1984),
    ([366], 1980),
    ([-366], 1980),
    ([-100], 1980),
    ([0], 1980),
    ([365], 1980),
    ([367], 1981),
    ([1000], 1982),
    ([1826], 1984),
    ([2000], 1985),
    ([3000], 1988),
    ([4000], 1990),
    ([5000], 1993),
    ([10592], 2008)
]

suites = {}

for n in [-1,1]:
    add_suite = TestSuite()
    for params, correct_out in test_cases_info:
        add_suite.add_test(ZuneNegateWithNthParamter(
            params, correct_out, n))
    suites[f"add_{n}"] = add_suite

inf_suite = TestSuite()
for params, correct_out in test_cases_info:
    inf_suite.add_test(ZuneInfiniteBug(
        params, correct_out))
    suites[f"infinite"] = inf_suite

