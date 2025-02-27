import unittest

from dummyfunction import add

class NumberTestCase(unittest.TestCase):

    def test_add_number(self):
        number = add(1, 1)
        self.assertEqual(number, 2)