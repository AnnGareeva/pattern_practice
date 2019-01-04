import os
import unittest
import sys
from subprocess import Popen, PIPE

# Нужен тест на функцию convert_digits
class DigitConverterTest(unittest.TestCase):
    def setUp(self):
        self.test_correct_input_list = [
            '._. ... ._. ._. ... ._. ._. ._.\n'
            '|.| ..| ._| ._| |_| |_. |_. ..|\n'
            '|_| ..| |_. ._| ..| ._| |_| ..|\n'
            '... ... ... ... ... ... ... ...',
        
            '._. ... ._. ._. ... ._. ._. ._. ._. ._.\n'
            '|.| ..| ._| ._| |_| |_. |_. ..| |_| |_|\n'
            '|_| ..| |_. ._| ..| ._| |_| ..| |_| ._|\n'
            '... ... ... ... ... ... ... ... ... ...\n'
            '._. ... ._. ._. ... ._. ._. ._. ._.\n'
            '|.| ..| ._| ._| |_| |_. |_. ..| |_|\n'
            '|_| ..| |_. ._| ..| ._| |_| ..| |_|\n'
            '... ... ... ... ... ... ... ... ...']

        self.expected_result = [
            '01234567',
            '0123456789012345678'
        ]

        self.test_incorrect_input_list = [
            '._. ... ._. ._. ... ._. ._. ._. ._. ._. ._.\n'
            '|.| ..| ._| ._| |_| |_. |_. ..| |_| |_| |.|\n'
            '|_| ..| |_. ._| ..| ._| |_| ..| |_| ._| |_|\n'
            '... ... ... ... ... ... ... ... ... ... ...',

            '._. ... ._. ._. ... ._. ._. ._.\n'
            '|.| ..| ._| ._| |_| |_. |_. |||\n'
            '|_| ..| |_. ._| ..| ._| |_| |||\n'
            '... ... ... ... ... ... ... ...',

            '._. ... ._. ._. ...\n'
            '|aa ..| ._| ._| |_|\n'
            '|_| ..| |_. ._| ..|\n'
            '... ... ... ...',
        ]

        self.test_correct_input_files = {
            'digits_example_1.txt' : '0123456789012345678',
            'digits_example_2.txt' : '012345678901234'
        }

        self.test_incorrect_input_files = [
            'digits_incorrect_example_1.txt',
            'digits_incorrect_example_2.txt',
            'digits_incorrect_example_3.txt',
        ]

    def test_correct_input_console(self):
        command = ["python", "lab_2.py"]
        for i in range(len(self.test_correct_input_list)):
            p = Popen(command, stdout=PIPE, stdin=PIPE)
            output = p.communicate(input=self.test_correct_input_list[i])[0]
            self.assertEqual(output.rstrip(), self.expected_result[i])

        out_file_name = 'test_correct_input_console.txt'
        command = ["python", "lab_2.py", '-o', out_file_name]
        for i in range(len(self.test_correct_input_list)):
            p = Popen(command, stdout=PIPE, stdin=PIPE)
            output = p.communicate(input=self.test_correct_input_list[i])[0]
            self.assertTrue(os.path.exists(out_file_name))
            with open(out_file_name, 'r') as f:
                output = f.readline()
            self.assertEqual(output.rstrip(), self.expected_result[i])
    
    def test_incorrect_input_console(self):
        command = ["python", "lab_2.py"]
        for i in range(len(self.test_incorrect_input_list)):
            p = Popen(command, stdout=PIPE, stdin=PIPE)
            output = p.communicate(input=self.test_incorrect_input_list[i])[0]
            self.assertNotEqual(p.returncode, 0)

    def test_correct_input_file(self):
        for file_name, result in self.test_correct_input_files.items():
            command = ["python", "lab_2.py", "-i", file_name]
            p = Popen(command, stdout=PIPE, stdin=PIPE)
            output = p.communicate()[0]
            self.assertEqual(output.rstrip(), result)

        out_file_name = 'test_correct_input_file.txt'
        for file_name, result in self.test_correct_input_files.items():
            command = ["python", "lab_2.py", "-i", file_name, "-o", out_file_name]
            p = Popen(command, stdout=PIPE, stdin=PIPE)
            p.communicate()
            self.assertTrue(os.path.exists(out_file_name))
            with open(out_file_name, 'r') as f:
                output = f.readline()
            self.assertEqual(output.rstrip(), result)

    def test_incorrect_input_file(self):
        for file_name in self.test_incorrect_input_files:
            command = ["python", "lab_2.py", "-i", file_name]
            p = Popen(command, stdout=PIPE, stdin=PIPE)
            output = p.communicate()[0]
            self.assertNotEqual(p.returncode, 0)

if __name__ == '__main__':
    unittest.main()