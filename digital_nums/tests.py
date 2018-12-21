import unittest
import os
import sys
import subprocess

class DigitalNumberTest(unittest.TestCase):
    script_name = 'digital_num_converter.py'

    def setUp(self):
        self.valid_input_terminal = "._. ... ._. ._. ... ._. ._. ._. ._.\n"\
                                    "|.| ..| ._| ._| |_| |_. |_. ..| |_|\n"\
                                    "|_| ..| |_. ._| ..| ._| |_| ..| |_|\n"\
                                    "... ... ... ... ... ... ... ... ...\n"\
                                    "._. ._. ._. ._. ._. ._. ._. ._. ...\n"\
                                    "|.| |.| |.| |.| |.| |.| |.| |_. ..|\n"\
                                    "|_| |_| |_| |_| |_| |_| |_| ._| ..|\n"\
                                    "... ... ... ... ... ... ... ... ...\n"\
                                    "._. ._. ._. ._. ._. ._. ._. ._. ...\n"\
                                    "|.| |.| |.| |_| |.| |.. |.| |_| ..|\n"\
                                    "|_| |_| |_| |_| |_| |_| |_| ._| ..|\n"\
                                    "... ... ... ... ... ... ... ... ...\n"

        self.valid_answer =   '012345678 error\n'\
                              '000000051\n'\
                              '00080?091 ill\n'
        self.valid_answer_file = '0???????? ill\n'\
                                 '000000051\n'\
                                 '012345678 error\n'
        self.invalid_count_num_input_terminal =  '._. ... ._. ._. ... ._. ._. ._. ._.\n'\
                                                 '|.| ..| ._| ._| |_| |_. |_. ..| |_|\n'\
                                                 '|_| ..| |_. ._| ..| ._| |_| ..| |_|\n'\
                                                 '... ... ... ... ... ... ... ... ...\n'\
                                                 '._. ._. ._. ._. ._. ._. ._. ._.\n'\
                                                 '|.| |.| |.| |.| |.| |.| |.| |_.\n'\
                                                 '|_| |_| |_| |_| |_| |_| |_| ._|'

        self.invalid_num_str_input_terminal =  '._. ... ._. ._. ... ._. ._. ._. ._.\n'\
                                               '|.| ..| ._| ._| |_| |_. |_. ..| |_|'

        self.invalid_symb_input_terminal =  'abc ... abc ._. ... ._. ._. ._. ._.\n'\
                                            '|.| ..| ._| ._| |_| |_. |_. ..| |_|\n'\
                                            '|_| abc |_. ._| ..| ._| |_| ..| |_|\n'\
                                            '... ... ... ... ... ... ... ... ...'
        self.invalid_answer = ''
        self.valid_input_file = '.\\valid_example.txt'
        self.invalid_count_num_input_file = '.\\inval_example1.txt.txt'
        self.invalid_num_str_input_file = '.\\inval_example2.txt'
        self.invalid_symb_input_file = '.\\inval_example3.txt'

    def test_valid_input_terminal_output_terminal(self):
        cmd = ['python', self.script_name]
        input_str = self.valid_input_terminal.encode()
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, err = proc.communicate(input=input_str)
        self.assertEqual(output.decode('utf8').replace('\r',''), self.valid_answer)

    def test_invalid_input_terminal_output_terminal(self):
        cmd = ['python', self.script_name]
        invalid_input_list = (self.invalid_count_num_input_terminal,
                              self.invalid_num_str_input_terminal,
                              self.invalid_symb_input_terminal)
        for input in invalid_input_list:
            proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, err = proc.communicate(input=input.encode())
            self.assertEqual(output.decode('utf8').replace('\r',''), self.invalid_answer)
    
    def test_valid_input_terminal_output_file(self):
        output_name_file = 'res.txt'
        cmd = ['python', self.script_name, '-o', output_name_file]
        input_data = self.valid_input_terminal.encode()
        proc = subprocess.run(cmd, input=input_data)
        with open(output_name_file, 'r') as f:
            data_from_files = f.read()
        self.assertEqual(data_from_files, self.valid_answer)
    
    
    def test_invalid_input_terminal_output_file(self):
        output_name_file = 'res.txt'
        cmd = ['python', self.script_name, '-o', output_name_file]
        invalid_input_list = (self.invalid_count_num_input_terminal,
                              self.invalid_num_str_input_terminal,
                              self.invalid_symb_input_terminal)
        for input_data in invalid_input_list:
            proc = subprocess.run(cmd, input=input_data.encode())
            try:   
                with open(output_name_file, 'r') as f:
                    data_from_files = f.read()
                self.assertTrue(False)
            except:
                self.assertTrue(True)
    
    def test_valid_input_file_output_terminal(self):
        cmd = ['python', self.script_name, '-i', self.valid_input_file]
        proc = subprocess.Popen(cmd,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = proc.communicate()
        self.assertEqual(output.decode('utf8').replace('\r',''), self.valid_answer_file)
    
    def test_invalid_input_file_output_terminal(self):
        input_files_list = (self.invalid_count_num_input_file, 
                            self.invalid_num_str_input_file, 
                            self.invalid_symb_input_file)
        for input_file in input_files_list:
            cmd = ['python', self.script_name, '-i', input_file]
            proc = subprocess.Popen(cmd,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, err = proc.communicate()
            self.assertEqual(output.decode('utf8').replace('\r',''), self.invalid_answer)
    
    def test_valid_input_file_output_file(self):
        output_name_file = 'res.txt'
        cmd = ['python', self.script_name, '-i', self.valid_input_file, '-o', output_name_file]
        proc = subprocess.run(cmd)  
        with open(output_name_file, 'r') as f:
            data_from_files = f.read()
        self.assertEqual(data_from_files, self.valid_answer_file)
    
    def test_invalid_input_file_output_file(self):
        output_name_file = 'res.txt'
        input_files_list = (self.invalid_count_num_input_file, 
                            self.invalid_num_str_input_file, 
                            self.invalid_symb_input_file)
        for input_file in input_files_list:
            cmd = ['python', self.script_name, '-i',input_file, '-o', output_name_file]
            proc = subprocess.run(cmd)
            try:   
                with open(output_name_file, 'r') as f:
                    data_from_files = f.read()
                self.assertTrue(False)
            except:
                self.assertTrue(True) 

if __name__ == '__main__':
    unittest.main()


