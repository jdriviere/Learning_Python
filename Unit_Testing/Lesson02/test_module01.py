import unittest

class TestClass01 (unittest.TestCase):
    def test_case01 (self):
        my_str = "This is JD"
        my_int = 999
        
        self.assertTrue (isinstance (my_str, str))
        self.assertTrue (isinstance (my_int, int))
    
    def test_case02 (self):
        my_pi = 3.14
        self.assertFalse (isinstance (my_pi, int))

# This is the Test-Runner
if __name__ == '__main__':
    unittest.main()

# NOTE: When running the code in the terminal (command prompt)
#       simply type:
#       python test_module01.py
#       Add -v if you want a verbose output.