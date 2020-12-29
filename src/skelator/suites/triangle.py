from ..test import Test, TestSuite


class TriangleTest(Test):
    valid = "Yes\n"
    invalid = "No\n"

    @property
    def correct_output(self):
        if self._correct_output:
            return self.valid
        else:
            return self.invalid

    @property
    def negation(self):
        if not self._correct_output:
            return self.valid
        else:
            return self.invalid


Triangle = TestSuite()
Triangle.add_test(TriangleTest([1, 2, 3, 1, 2, 3], False))
Triangle.add_test(TriangleTest([1, 2, 3, 3, 2, 1], True))
Triangle.add_test(TriangleTest([1, 3, 3, 3, 3, 1], True))
Triangle.add_test(TriangleTest([1, 1, 1, 1, 1, 1], False))

