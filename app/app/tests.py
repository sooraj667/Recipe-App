""" Runs the test cases """
from django.test import SimpleTestCase
from . import calc
class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_two_numbers(self):
        """tests adding the two numbers"""
        res = calc.add_two_numbers(5,5)
        self.assertEqual(res, 10)









