"""
test fixtures are the set of steps performed before and after the tests.
In unittest, these are implemented as methods of the TestCase class and can be
overridden for your purposes.
"""

import unittest


def setUpModule():
    """
    Called ONCE, BEFORE anything else in this module.
    """
    print('We are in the setUpModule()!')


def tearDownModule():
    """
    Called ONCE, AFTER everything else in this module.
    """
    print('We are in the tearDownModule()!')


class TestClass06(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Called ONCE, BEFORE any tests!
        """
        print('We are in the setUpClass()!')

    @classmethod
    def tearDownClass(cls):
        """
        Called ONCE, AFTER all tests -- if setUpClass() was successful!
        """
        print('We are in the tearDownClass()!')

    def setUp(self):
        """
        Called MULTIPLE TIME, BEFORE every test method!
        """
        print('\nWe are in the setUp()!')

    def tearDown(self):
        """
        Called MULTIPLE TIMES, AFTER every test method!
        """
        print('\nWe are in the tearDown()!')

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())

    def test_case02(self):
        self.assertFalse("python".isupper())


if __name__ == '__main__':
    unittest.main()

"""
NOTE:
- The setUpModule() and tearDownModule() methods are the
module-level fixtures.
- The setUpModule() is executed before any method in the test module.
- The tearDownModule() is executed after all methods in the test module.
The setUpClass() and the tearDownClass() are class-level fixtures.
- The setUpClass() is executed before any method in
the test class.
- The tearDownClass() is executed after all methods in the test class. (p.38)
"""
