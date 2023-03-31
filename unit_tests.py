import unittest
import number_calculation

class TestConvertNumberToWords(unittest.TestCase):
    #first test for one digit implementation 0-9
    def test_convert_one_digit(self):
        self.assertEqual(number_calculation.convert_one_digit(0), 'zero')
        self.assertEqual(number_calculation.convert_one_digit(1), 'one')
        self.assertEqual(number_calculation.convert_one_digit(9), 'nine')

    #second test cases for two digit implementation 0-99
    def test_convert_two_digits(self):
        self.assertEqual(number_calculation.convert_two_digits(0), 'zero')
        self.assertEqual(number_calculation.convert_two_digits(12), 'twelve')
        self.assertEqual(number_calculation.convert_two_digits(17), 'seventeen')
        self.assertEqual(number_calculation.convert_two_digits(21), 'twenty one')
        self.assertEqual(number_calculation.convert_two_digits(50), 'fifty')
        self.assertEqual(number_calculation.convert_two_digits(99), 'ninety nine')

    #third test cases for three digit implementation 0-999
    def test_convert_three_digits(self):
        self.assertEqual(number_calculation.convert_three_digits(0), 'zero')
        self.assertEqual(number_calculation.convert_three_digits(99), 'ninety nine')
        self.assertEqual(number_calculation.convert_three_digits(100), 'one hundred')
        self.assertEqual(number_calculation.convert_three_digits(101), 'one hundred and one')
        self.assertEqual(number_calculation.convert_three_digits(110), 'one hundred and ten')
        self.assertEqual(number_calculation.convert_three_digits(999), 'nine hundred and ninety nine')
    
    #fourth test cases for all digit implementation (focus on 1000-999999999 cause testcases 1-3 cover the others)
    def test_convert_all_digits(self):
        self.assertEqual(number_calculation.convert_number_to_words(0), 'zero')
        self.assertEqual(number_calculation.convert_number_to_words(9), 'nine')
        self.assertEqual(number_calculation.convert_number_to_words(99), 'ninety nine')
        self.assertEqual(number_calculation.convert_number_to_words(999), 'nine hundred and ninety nine')
        self.assertEqual(number_calculation.convert_number_to_words(1000), 'one thousand')
        self.assertEqual(number_calculation.convert_number_to_words(1001), 'one thousand one')
        self.assertEqual(number_calculation.convert_number_to_words(9999), 'nine thousand nine hundred and ninety nine')
        self.assertEqual(number_calculation.convert_number_to_words(10000), 'ten thousand')
        self.assertEqual(number_calculation.convert_number_to_words(99999), 'ninety nine thousand nine hundred and ninety nine')
        self.assertEqual(number_calculation.convert_number_to_words(100000), 'one hundred thousand')
        self.assertEqual(number_calculation.convert_number_to_words(999999), 'nine hundred and ninety nine thousand nine hundred and ninety nine')
        self.assertEqual(number_calculation.convert_number_to_words(1000000), 'one million')
        self.assertEqual(number_calculation.convert_number_to_words(9999999), 'nine million nine hundred and ninety nine thousand nine hundred and ninety nine')
        self.assertEqual(number_calculation.convert_number_to_words(10000000), 'ten million')
        self.assertEqual(number_calculation.convert_number_to_words(99999999), 'ninety nine million nine hundred and ninety nine thousand nine hundred and ninety nine')
        self.assertEqual(number_calculation.convert_number_to_words(100000000), 'one hundred million')
        self.assertEqual(number_calculation.convert_number_to_words(999999999), 'nine hundred and ninety nine million nine hundred and ninety nine thousand nine hundred and ninety nine')


unittest.main()