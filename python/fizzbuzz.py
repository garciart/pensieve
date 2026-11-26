"""An example of the FizzBuzz word game written in Python.

It creates a list numbers from 1 to an upper limit to STDOUT, replacing
numbers with 'fizz', 'buzz', or both if divisible by 3 or 5.

Note: This script has elements that you would not need or use for a
simple FizzBuzz program, like classes and unit tests. These elements
are included to demonstrate additional best practices.

Requirements:
- Python 3.6 or above.

Usage:

- Check the code for errors: `pylint fizzbuzz.py`
- Test the code: `python -B fizzbuzz.py test`
- Run with default upper limit (15): `python -B fizzbuzz.py`
- Run with an upper limit of 30: `python -B fizzbuzz.py 30`

NOTE: The -B option prevents Python from generating a `__pycache__` bytecode directory.
"""
import sys
import unittest

# Best Practice: Use constants for values used more than once
LIMIT_ERR_MSG = 'Invalid upper limit; enter an integer greater than 0.'

class FizzBuzz():
    """FizzBuzz word game class"""

    # Best Practice: Use type hinting
    def __init__(self, verbose: bool = True) -> None:
        # Best Practice: Use docstrings (we use reStructuredText)
        """Instantiates the class and initialize the class variables.

        :param bool verbose: Show numbers during run, defaults to true, defaults to True.
        """
        # Best Practice: Validate inputs
        if not isinstance(verbose, bool):
            raise ValueError('Verbosity option must be true or false.')

        # Set class variable
        self.verbose = verbose

    def run(self, limit: int = 15) -> list:
        """Creates a list of numbers from 1 to an upper limit, replacing
        numbers with 'fizz', 'buzz', or both if divisible by 3 or 5.

        :param int limit: Upper limit for the loop, defaults to 15.

        :return list: A list of numbers and substitutions
        """
        # Validate inputs
        if not isinstance(limit, int) or limit < 1:
            raise ValueError(LIMIT_ERR_MSG)

        # Best Practice:
        #   DO NOT USE LEET CODE LIKE THIS!
        #   _list_of_results = ['Fizz'*(not i%3) + 'Buzz'*(
        #       not i%5) or i for i in range(1, self.limit + 1)]
        # Use readable code like this:

        # Initialize scope variables
        # Bast Practice: Add leading underscores to restricted variables
        _list_of_results = []

        for _i in range(1, limit + 1):
            # Instantiate scope variables
            _output = ''

            # Append 'fizz', 'buzz', or both to _output if applicable
            if _i % 3 == 0:
                _output += 'fizz'
            if _i % 5 == 0:
                _output += 'buzz'

            # Set _output to the number if not divisible by 3 or 5
            if _output == '':
                _output = f'{_i}'

            # Append the output to the result list
            _list_of_results.append(_output)

            # Show the value
            if self.verbose:
                print(_output)

        return _list_of_results

# Best Practice: Use unit tests
class TestFizzBuzzFunction(unittest.TestCase):
    """Test suite for fizzbuzz.py
    """
    def test_fizzbuzz_init_pass_arg(self):
        """Test that init method accepts valid arguments"""
        FizzBuzz(verbose=True)

    def test_fizzbuzz_init_pass_noarg(self):
        """Test that init method uses default arguments"""
        FizzBuzz()

    def test_fizzbuzz_init_fail_none_arg(self):
        """Test that init detects None args"""
        with self.assertRaises(ValueError):
            FizzBuzz(verbose=None)

    def test_fizzbuzz_init_fail_wrong_type(self):
        """Test that init detects args of the wrong type"""
        with self.assertRaises(ValueError):
            FizzBuzz(verbose='a')
        with self.assertRaises(ValueError):
            FizzBuzz(verbose=1)

    def test_fizzbuzz_run_pass_arg(self):
        """Test that run method accepts valid arguments"""
        _fizzbuzz = FizzBuzz()
        _fizzbuzz.run(limit=20)

    def test_fizzbuzz_run_pass_noarg(self):
        """Test that run method uses default arguments"""
        _fizzbuzz = FizzBuzz()
        _fizzbuzz.run()

    # Add 'noqa' to the end of lines with invalid values for testing

    def test_fizzbuzz_run_fail_none_arg(self):
        """Test that run method detects None args"""
        _fizzbuzz = FizzBuzz()
        with self.assertRaises(ValueError):
            _fizzbuzz.run(limit=None)  # noqa

    def test_fizzbuzz_run_fail_wrong_type(self):
        """Test that run method detects args of the wrong type"""
        _fizzbuzz = FizzBuzz()
        with self.assertRaises(ValueError):
            _fizzbuzz.run(limit='a')  # noqa

    def test_fizzbuzz_run_fail_less_than_1(self):
        """Test that run method detects 0 or negative args"""
        _fizzbuzz = FizzBuzz()
        with self.assertRaises(ValueError):
            _fizzbuzz.run(limit=0)
        with self.assertRaises(ValueError):
            _fizzbuzz.run(limit=-1)



if __name__ == '__main__':
    # Initialize scope variables
    upper_limit = 15  # pylint: disable=invalid-name

    # Get command-line arguments, if any
    if len(sys.argv) > 1:
        if sys.argv[1].strip().lower() == 'test':
            # Run tests and exit
            # Note: Send an empty argument list to unittest.main
            # or it will try to apply sys.argv, causing an error
            unittest.main(argv=[''], exit=True)
        else:
            # Invalid arguments will be caught later
            upper_limit = sys.argv[1]

    try:
        # Instantiate the FizzBuzz class
        fizzbuzz = FizzBuzz(verbose=True)
        # Run FizzBuzz
        result = fizzbuzz.run(limit=int(upper_limit))
        # Capture and show the results
        print('Result', type(result), result)
    except ValueError as e:
        print(LIMIT_ERR_MSG)
    finally:
        print('All done! Have a nice day.')
