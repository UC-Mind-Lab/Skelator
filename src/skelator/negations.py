from .test import Test


class NegateWithNthParameter(Test):
    def __init__(self, parameters, correct_output, nth_parameter):
        """Test case
        
        Parameters
        ----------
        parameters: list
            The parameters for the test case
        correct_output: any
            The correct output given the parameters
        nth_parameter
            The nth parameter to return as the negation
        """
        super().__init__(parameters, correct_output)
        self.nth_parameter = nth_parameter
        if not 0 <= nth_parameter < len(parameters):
            raise ValueError(f"nth_parameter of {nth_parameter} is not "\
                    f"valid as there are {len(parameters)} parameters")

    @property
    def _negation(self):
        return self.parameters[self.nth_parameter]

