# pylint
# pyflakes (used by repl to lint)
# PEP 8 - standard style guide for Python

# now that it stands up, let's make it strong
import unittest
import main


class TestMain(unittest.TestCase):
    # setUp() defines a... you guessed it, setup block of code to be run before the rest of the tests. good for default vars or something similar.
    def setUp(self):
        print('about to test the function')

    def test_add_five(self):
        test_param = 10
        result = main.add_five(test_param)
        # we inherit assertEqual from TestCase
        self.assertEqual(result, 15)

    def test_add_five_string(self):
        test_param = 'asdfasdfs'
        result = main.add_five(test_param)
        # we inherit assertEqual from TestCase

        # note the use of isinstance to check ValueError, as what is returned is an instance of a ValueError, and not the actual ValueError class, so this would fail the assertion without it

        # self.assertEqual(isinstance(result, ValueError)) won't work because of the expectation of two  arguments

        self.assertIsInstance(result, ValueError)

    def test_add_five_3(self):
        test_param = None
        result = main.add_five(test_param)
        self.assertEqual(result, "please enter number")

    def test_add_five_4(self):
        test_param = ''
        result = main.add_five(test_param)
        self.assertEqual(result, "please enter number")

    def tearDown(self):
        print('cleaning up')


# the if statement allows the bundling of these tests with the "python3 -m unittest" shell command.  -v for verbose flag
if __name__ == "__main__":
    unittest.main()
