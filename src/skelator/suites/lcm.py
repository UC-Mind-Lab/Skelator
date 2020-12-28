from ..test import Test, TestSuite


class LCMTest(Test):
    @property
    def correct_output(self):
        return f"{self._correct_output}\n"

    @property
    def negation(self):
        return f"{self.parameters[0]}\n"


LCM = TestSuite()
LCM.add_test(LCMTest([1071, 1029], 52479))
LCM.add_test(LCMTest([555, 666], 3330))
LCM.add_test(LCMTest([678, 987], 223062))
LCM.add_test(LCMTest([8767, 653], 5724851))
LCM.add_test(LCMTest([16777216, 512], 16777216))
LCM.add_test(LCMTest([16, 4], 16))
LCM.add_test(LCMTest([315, 831], 87255))
LCM.add_test(LCMTest([513332, 91583315],
    "Error: An overflow has occurred."))
LCM.add_test(LCMTest([112, 135], 15120))
LCM.add_test(LCMTest([310, 55], 3410))
LCM.add_test(LCMTest([0, 55], 0))
LCM.add_test(LCMTest([55, 0], 0))

