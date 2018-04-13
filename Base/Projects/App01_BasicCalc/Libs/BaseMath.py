"""
@name Test_BaseMath
@author J. D. Riviere
@date 12/30/2017
A simple Calculator App that performs the most basic arithmetic functions.
"""

class Calc:
    """
    This is a basic calculator for basic arithmetics.
    """

    # Member functions
    def add_it(self, num1, num2):
        """
        Basic addition arithmetic operation.
        """
        var_type = (int, float) # To ensure the accepted var types are integers or floats

        # Use isinstance() function to compare variable with a comparative (var_type)
        if isinstance(num1, var_type) and isinstance(num2, var_type):
            return num1 + num2
        else:
            # Raise a ValueError exception, because proper value type was not found
            raise ValueError("You tried implementing a value that is neither a float nor an integer!")
    
    def sub_it (self):
        pass
    
    def mul_it (self):
        pass
    
    def div_it (self):
        pass