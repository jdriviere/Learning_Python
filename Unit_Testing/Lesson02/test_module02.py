import unittest
import inspect


class TestClass02(unittest.TestCase):
    def test_case02(self):
        """
        "inspect.stack()[0][3] method prints the name of
        the current test method. It's useful when you want
        to know the order that the methods are executed
        in the class." (p.34)
        """
        print('\nRunning Test Method:', inspect.stack()[0][3])

    def test_case01(self):
        print('\nRunning Test Method:', inspect.stack()[0][3])


if __name__ == '__main__':
    unittest.main(verbosity=2)

# NOTE: The test methods will run in alphabetical order,
#       irrespective of the test methods in the code.
