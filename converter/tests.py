from num_converter import Converter
import unittest


class RomanToArabConverterTest(unittest.TestCase):
    def setUp(self):
        self.conv = Converter()

    def test_valid_input(self):
		# Данные примеры не являются корректными римскими числами
		# Также непллохо бы отдельно написать тесты на функцию проверки
		# Корректности числа
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


class ArabToRomanConverterTest(unittest.TestCase):
    def setUp(self):
        self.conv = Converter()


    def test_valid_input(self):
		# Этот тест фейлится с IndexError: list index out of range
        self.assertEqual(self.conv.arab_to_roman(317),  'CCCXVII')
        self.assertEqual(self.conv.arab_to_roman(199),  'CXCIX')
        self.assertEqual(self.conv.arab_to_roman(149),  'CXLIX')
        self.assertEqual(self.conv.arab_to_roman(1721), 'MDCCXXI')
        self.assertEqual(self.conv.arab_to_roman(2975), 'MMCMLXXV')


    def test_invalid_input(self):
        try:
            self.conv.arab_to_roman('432a')
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            self.conv.arab_to_roman('')
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            self.conv.arab_to_roman(-3)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)


    def test_overflow(self):
        try:
            self.conv.arab_to_roman('43242')
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()