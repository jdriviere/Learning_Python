import unittest


class TestClass07(unittest.TestCase):
    def test_case01(self):
        self.assertTrue('PYTHON'.isupper())
        print('\nIn Test_Case01()!')


"""
NOTE:
"If you try to run it the usual way, with python3 test_module06.py, you do not get
output in the console, as it does not have the if __name__=='__main__' and unittest.
main() statements in it. Even running in verbose mode with python3 test_module06.py
-v does not yield any output in the console.

The only way to run this module is to use the Python interpreter with the -m
unittest option and the module name, as follows:

python -m unittest test_module06" (p.40)

"""
