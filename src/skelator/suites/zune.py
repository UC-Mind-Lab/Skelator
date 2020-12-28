from ..test import Test, TestSuite

class ZuneTest(Test):
    output_sentence = "current year is"
    @property
    def negation(self):
        return f"{self.output_sentence} {self._correct_output + 1}\n"

    @property
    def correct_output(self):
        return f"{self.output_sentence} {self._correct_output}\n"


ZUNE = TestSuite()
ZUNE.add_test(ZuneTest([10593], 2008))
ZUNE.add_test(ZuneTest([12054], 2012))
ZUNE.add_test(ZuneTest([1827], 1984))
ZUNE.add_test(ZuneTest([366], 1980))
ZUNE.add_test(ZuneTest([-366], 1980))
ZUNE.add_test(ZuneTest([-100], 1980))
ZUNE.add_test(ZuneTest([0], 1980))
ZUNE.add_test(ZuneTest([365], 1980))
ZUNE.add_test(ZuneTest([367], 1981))
ZUNE.add_test(ZuneTest([1000], 1982))
ZUNE.add_test(ZuneTest([1826], 1984))
ZUNE.add_test(ZuneTest([2000], 1985))
ZUNE.add_test(ZuneTest([3000], 1988))
ZUNE.add_test(ZuneTest([4000], 1990))
ZUNE.add_test(ZuneTest([5000], 1993))
ZUNE.add_test(ZuneTest([10592], 2008))

