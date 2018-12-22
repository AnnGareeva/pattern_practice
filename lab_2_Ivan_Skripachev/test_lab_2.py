import os
import unittest
import sys
from subprocess import Popen, PIPE

class DigitConverterTest(unittest.TestCase):
    def setUp(self):
        self.test_correct_input_list = [
            ' _       _   _       _   _   _   _ \n'
            '| |   |  _|  _| |_| |_  |_    | |_|\n'
            '|_|   | |_   _|   |  _| |_|   | |_|\n'
            '                                   ',
        
            '     _   _       _   _   _   _   _ \n'
            '  |  _|  _| |_| |_  |_    | |_| |_|\n'
            '  | |_   _|   |  _| |_|   | |_| |_|\n'
            '                                   \n'
            ' _   _   _   _   _   _   _   _     \n'
            '| | | | | | | | | | | | | | |_    |\n'
            '|_| |_| |_| |_| |_| |_| |_|  _|   |\n'
            '                                   \n'
            ' _   _   _   _   _   _   _   _   _ \n'
            '|_| | | | | |_  | | | | | |  _| | |\n'
            ' _| |_| |_| |_| |_| |_| |_| |_  |_|\n'
            '                                   ']

        self.expected_correct_result = [
            '012345678 ERROR',
            '123456788 ERROR\n'
            '000000051\n'
            '900600020'
        ]

        self.test_incorrect_input_list = [
            ' _       _   _       _   _   _   _ \n'
            '| |      _|  _|  _| |_  |     | |_|\n'
            '|_|   | |_   _|   |  _| |_|   | |_|\n'
            '                                   ',

            ' _       _   _       _   _       _ \n'
            '| |   |  _|  _|     |_  |_      |_|\n'
            '|_|   | |_   _|      _| |_|     |_|\n'
            '                                   ',

            ' _       _   _       _   _   _   _ \n'
            '|aa   |  _\  BB |_| 178 |_    | |_|\n'
            '|_|   | |_   _|   |  _| *_*   | |_|\n'
            '                                   '
        ]

        self.expected_incorrect_result = [
            '0?23?5?78 ILL',
            '0123?56?8 ILL',
            '?1??4??78 ILL'
        ]

        self.test_correct_input_files = {
            'digits_example_1.txt' : '012345678 ERROR\n'
                                     '123456789',
            'digits_example_2.txt' : '900600020'
        }

        self.test_incorrect_input_files = {
            'digits_incorrect_example_1.txt' : '?0000?0?1 ILL',
            'digits_incorrect_example_2.txt' : '01?345678 ILL',
            'digits_incorrect_example_3.txt' : '0?2?456?? ILL'
        }

    def test_correct_input_console(self):
        # Input console | Output to console
        command = ["python", "lab_2.py"]
        for i in range(len(self.test_correct_input_list)):
            p = Popen(command, stdout=PIPE, stdin=PIPE)
            output = p.communicate(input=self.test_correct_input_list[i])[0]
            self.assertEqual(output.rstrip(), self.expected_correct_result[i])

        # Input console | Output to file
        out_file_name = 'test_correct_input_console.txt'
        command = ["python", "lab_2.py", '-o', out_file_name]
        for i in range(len(self.test_correct_input_list)):
            p = Popen(command, stdout=PIPE, stdin=PIPE)
            output = p.communicate(input=self.test_correct_input_list[i])[0]
            self.assertTrue(os.path.exists(out_file_name))
            with open(out_file_name, 'r') as f:
                output = f.read()
            self.assertEqual(output.rstrip(), self.expected_correct_result[i])
    
    def test_incorrect_input_console(self):
        # Input console incorrect
        command = ["python", "lab_2.py"]
        for i in range(len(self.test_incorrect_input_list)):
            p = Popen(command, stdout=PIPE, stdin=PIPE)
            output = p.communicate(input=self.test_incorrect_input_list[i])[0]
            self.assertEqual(output.rstrip(), self.expected_incorrect_result[i])

    def test_correct_input_file(self):
        # Input file | Output to console
        for file_name, result in self.test_correct_input_files.items():
            command = ["python", "lab_2.py", "-i", file_name]
            p = Popen(command, stdout=PIPE, stdin=PIPE)
            output = p.communicate()[0]
            self.assertEqual(output.rstrip(), result)

        # Input file | Output to file
        out_file_name = 'test_correct_input_file.txt'
        for file_name, result in self.test_correct_input_files.items():
            command = ["python", "lab_2.py", "-i", file_name, "-o", out_file_name]
            p = Popen(command, stdout=PIPE, stdin=PIPE)
            p.communicate()
            self.assertTrue(os.path.exists(out_file_name))
            with open(out_file_name, 'r') as f:
                output = f.read()
            self.assertEqual(output.rstrip(), result)

    def test_incorrect_input_file(self):
        # Input file incorrect
        for file_name, result in self.test_incorrect_input_files.items():
            command = ["python", "lab_2.py", "-i", file_name]
            p = Popen(command, stdout=PIPE, stdin=PIPE)
            output = p.communicate()[0]
            self.assertEqual(output.rstrip(), result)

if __name__ == '__main__':
    unittest.main()