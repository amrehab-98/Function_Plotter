import unittest
from functions import callback_isdigit


class TestFunctions(unittest.TestCase):
    def test_callback_isdigit_none_digit_input(self):
        result = callback_isdigit("x")
        self.assertFalse(result)

    def test_callback_isdigit_positive_int_input(self):
        result = callback_isdigit("55")
        self.assertTrue(result)

    def test_callback_isdigit_negative_int_input(self):
        result = callback_isdigit("-55")
        self.assertTrue(result)

    def test_callback_isdigit_positive_float_input(self):
        result = callback_isdigit("55.19")
        self.assertTrue(result)

    def test_callback_isdigit_negative_float_input(self):
        result = callback_isdigit("-55.19")
        self.assertTrue(result)

    def test_callback_isdigit_mix_input(self):
        result = callback_isdigit("mix of chars and 1239")
        self.assertFalse(result)

    def test_callback_isdigit_empty_input(self):
        result = callback_isdigit("")
        self.assertTrue(result)

    def test_callback_isdigit_space_input(self):
        result = callback_isdigit("  ")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
