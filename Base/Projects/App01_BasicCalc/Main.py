"""
@name Main.py
@author J. D. Riviere
@date 12/30/2017
"""

# Import libraries
try:
    from Libs.BaseMath import Calc # Import the entire file, to avoid using the wildcard (*)
except ImportError as error:
    print("ERROR: One or more modules failed to be imported!")
    print("Detailed error -->", error)
else:
    # Create object instance
    calc = Calc() # object = (Folder_Name).Imported_Library.Class_Name()
    num1 = 6
    num2 = -4

    # Test Functions
    print("{} + {} = {}".format(num1, num2, calc.add_it(num1, num2)))