from ..test import Test, TestSuite


class NthPrimeTest(Test):
    @staticmethod
    def output(nth, prime):
        return f"{nth}th prime number is {prime}\n"

    @property
    def correct_output(self):
        return self.output(self.parameters[0], self._correct_output)

    @property
    def negation(self):
        return self.output(self.parameters[0], self.parameters[0])


NthPrime = TestSuite(links="-lm")
NthPrime.add_test(NthPrimeTest([1], 2))
NthPrime.add_test(NthPrimeTest([2], 3))
NthPrime.add_test(NthPrimeTest([3], 5))
NthPrime.add_test(NthPrimeTest([4], 7))
NthPrime.add_test(NthPrimeTest([5], 11))
NthPrime.add_test(NthPrimeTest([6], 13))
NthPrime.add_test(NthPrimeTest([7], 17))
NthPrime.add_test(NthPrimeTest([8], 19))
NthPrime.add_test(NthPrimeTest([9], 23))
NthPrime.add_test(NthPrimeTest([10], 29))
NthPrime.add_test(NthPrimeTest([11], 31))
NthPrime.add_test(NthPrimeTest([12], 37))
NthPrime.add_test(NthPrimeTest([13], 41))
NthPrime.add_test(NthPrimeTest([14], 43))
NthPrime.add_test(NthPrimeTest([15], 47))
NthPrime.add_test(NthPrimeTest([16], 53))
NthPrime.add_test(NthPrimeTest([17], 59))
NthPrime.add_test(NthPrimeTest([18], 61))
NthPrime.add_test(NthPrimeTest([19], 67))
NthPrime.add_test(NthPrimeTest([20], 71))

