from num_converter import Converter
import unittest


class RomanToArabConverterTest(unittest.TestCase):
    def setUp(self):
        self.conv = Converter()

    def test_valid_input(self):
        self.assertEqual(self.conv.roman_to_arab('IIIII'), 5)
        self.assertEqual(self.conv.roman_to_arab('IXI'), 10)
        self.assertEqual(self.conv.roman_to_arab('VXICL'), 154)
        self.assertEqual(self.conv.roman_to_arab('XICL'), 159)
        self.assertEqual(self.conv.roman_to_arab('CILIXIIII'), 162)

    def test_invalid_input(self):
        try:
            self.conv.roman_to_arab('GHIlC')
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            self.conv.roman_to_arab('')
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            self.conv.roman_to_arab(157)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_overflow(self):
        try:
            self.conv.roman_to_arab('IMMMCCLL')
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()