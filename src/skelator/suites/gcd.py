from ..test import Test, TestSuite


class GCDTest(Test):
    @property
    def correct_output(self):
        return f"{self._correct_output}\n"

    @property
    def negation(self):
        return f"{self.parameters[0]}\n"


GCD = TestSuite()
GCD.add_test(GCDTest([1071, 1029], 21))
GCD.add_test(GCDTest([555, 666], 111))
GCD.add_test(GCDTest([678, 987], 3))
GCD.add_test(GCDTest([8767, 653], 1))
GCD.add_test(GCDTest([16777216, 512], 512))
GCD.add_test(GCDTest([16, 4], 4))
GCD.add_test(GCDTest([315, 831], 3))
GCD.add_test(GCDTest([513332, 91583315], 1))
GCD.add_test(GCDTest([112, 135], 1))
GCD.add_test(GCDTest([310, 55], 5))
GCD.add_test(GCDTest([0, 55], 55))

