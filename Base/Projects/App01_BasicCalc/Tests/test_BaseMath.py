"""
@name Test_BaseMath
@author J. D. Riviere
@date 12/30/2017
A series of tests to ensure quality of BaseMath class and functions.
"""

try:
    import pytest
    from Libs.BaseMath import Calc
except ImportError as error:
    print ("Error: Could not import one or more modules!")
    print ("Detailed error --> ", error)
else:
    class TestBaseMath (object):
        """
        A series of test to ensure proper functionality of BaseMath
        class and its functions.
        """

        def test_add_case1 (self):
            """
            First case of Add_It function: Correct/Passing case.
            --> BOTH variables are floats or integers.
            """
            calc = Calc().add_it (1, 1)
            assert calc == 2
        
        def test_add_case2 (self):
            """
            Second case of Add_It function: Incorrect/Failing case.
            --> First variable is neither a float nor an integer.
            """
            with pytest.raises (ValueError):
                calc = Calc().add_it ("1", 1)
        
        def test_add_case3 (self):
            """
            Third case of Add_It function: Incorrect/Failing case.
            --> Second variable is neither a float nor an integer.
            """
            with pytest.raises (ValueError):
                calc = Calc().add_it (1, "1")
        
        def test_add_case4 (self):
            """
            Fourth case of Add_It function: Incorrect/Failing case.
            --> NEITHER variables are floats nor integers.
            """
            with pytest.raises (ValueError):
                calc = Calc().add_it ("1", "1")