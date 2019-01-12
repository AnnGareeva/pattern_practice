import argparse
from functools import reduce
import os
import sys
from itertools import product

__all__ = ['convert_digital_nums']
NUM_IN_LINE = 9
NUMBER_SIZE = 3
INDENT_SIZE = 1


class DigitalNumber:
    matching_num_dict = {'0': [True,  True,  True,  True,  True,  False, True],
                         '1': [False, False, True,  True,  False, False, False],
                         '2': [False, True,  True,  False, True,  True,  True],
                         '3': [False, False, True,  True,  True,  True,  True],
                         '4': [True,  False, True,  True,  False, True,  False],
                         '5': [True,  False, False, True,  True,  True,  True],
                         '6': [True,  True,  False, True,  True,  True,  True],
                         '7': [False, False, True,  True,  True,  False, False],
                         '8': [True,  True,  True,  True,  True,  True,  True],
                         '9': [True,  False, True,  True,  True,  True,  True]}

    def __init__(self):
        self.left_up       = None
        self.left_down     = None
        self.right_up      = None
        self.right_down    = None
        self.center_up     = None
        self.center_middle = None
        self.center_down   = None
        self.number        = None
        self.digital_num   = None

    def convert_to_num(self):
        for key, value in self.matching_num_dict.items():
            if value == self.digital_num:
                res_number = int(key)
                self.number = res_number
                break

    def set_flag_list(self, digital_num_str):
        horiz_line = '_'
        vert_line = '|'
        self.left_up       = True if vert_line  == digital_num_str[1][0] else False
        self.left_down     = True if vert_line  == digital_num_str[2][0] else False
        self.right_up      = True if vert_line  == digital_num_str[1][2] else False
        self.right_down    = True if vert_line  == digital_num_str[2][2] else False
        self.center_up     = True if horiz_line == digital_num_str[0][1] else False
        self.center_middle = True if horiz_line == digital_num_str[1][1] else False
        self.center_down   = True if horiz_line == digital_num_str[2][1] else False
        position_list = [self.left_up,
                         self.left_down,
                         self.right_up,
                         self.right_down,
                         self.center_up,
                         self.center_middle,
                         self.center_down]
        self.digital_num = position_list

    def digital2num(self, digital_num_str):
        self.set_flag_list(digital_num_str)
        self.convert_to_num()
        return self.number


def convert_list2str(list_elem):
    string = str(reduce((lambda x, y: str(x) + str(y)), list_elem))
    return string


def check_valid_symbols(data):
    valid_symb = ['\n', ' ', '|', '_', '.']
    for string in data:
        for el in string:
            if not el in valid_symb:
                raise Exception('Invalid symbol \"{symb}\" in source data'.format(symb=el))


def check_valid_line_len(data):
    for string in data:
        if (len(string) != NUM_IN_LINE * (NUMBER_SIZE + INDENT_SIZE) and
            len(string) != NUM_IN_LINE * (NUMBER_SIZE + INDENT_SIZE) - INDENT_SIZE):
            raise Exception('Invalid legth of string. String must be 36 or 35 symbols')


def check_valid_num_strs(data):
    if (len(data) % (NUMBER_SIZE + INDENT_SIZE) != 0 and
        len(data) % (NUMBER_SIZE + INDENT_SIZE) != NUMBER_SIZE):
        raise Exception("Invalid number of strings. Height of number is 3, height of indent is 1 string")

    
def del_serv_char(data):
    for i in range(len(data)):
        line = data[i]
        if '\n' in line:
            line = line.replace('\n', '')
            data[i] = line
    return data


def validation(data):
    check_valid_line_len(data)
    check_valid_num_strs(data)
    check_valid_symbols(data)
    return True
  

def read_from_file(filename):
    if not os.path.exists(filename):
        raise Exception('{filename} does not exist'.format(filename=filename))
    with open(filename, 'r') as input_file:
        data = input_file.readlines()
    data = del_serv_char(data)
    validation(data)
    return data


def read_from_terminal():
    data = []
    for line in sys.stdin:
        data.append(line)
    data = del_serv_char(data)
    validation(data)
    return data


def write_to_file(list_num, filename):
    with open(filename, 'w') as f:
        for line in list_num:
            for var in line:
                f.writelines(var)
                f.write('\n')


def write_to_terminal(list_num):
    for line in list_num:
        for var in line:
            print(var)


def check_sum(numbers):
    weighted_list = [numbers[idx] * (NUM_IN_LINE - idx) for idx in range(NUM_IN_LINE)]
    weighted_sum  = sum(weighted_list)
    if weighted_sum % 11 == 0:
        return convert_list2str(numbers)
    else:
        return '{num} error'.format(num=convert_list2str(numbers))


def count_dif_vals(list1, list2):
    dif_counter = 0
    dif_idx = None
    for idx in range(len(list1)):

        if list1[idx] != list2[idx]:
            dif_counter += 1
            dif_idx = idx
    if dif_counter < 2:
        return dif_idx
    else:
        return None




def recover_none_num(dg_num_obj, digital_number):
    dg_num_obj.set_flag_list(digital_number)
    varients_list = []
    for key, val in dg_num_obj.matching_num_dict.items():
        dif_flag = count_dif_vals(val, dg_num_obj.digital_num) 
        if dif_flag:
            varients_list.append(int(key))
    if not varients_list:
        return ['None']
    return varients_list


def processing_line(parsed_num_list, flag_none_in_line):
    checked_num_list = []
    for card_num in parsed_num_list:
        if 'None' not in card_num:
            result_str = check_sum(card_num)
            if flag_none_in_line and 'error' not in result_str:
                    result_str += ' recovered'
        else:
            result_str = convert_list2str(card_num).replace('None', '?') + ' ill'
        checked_num_list.append(result_str)
    return checked_num_list


def convert_data_to_num_list(data):
    start_vertical = 0
    num_list = []
    while start_vertical < len(data):
        start_horizontal = 0
        num_seq = []
        flag_none_in_line = False
        while start_horizontal < len(data[start_vertical]):
            varients_of_number = []
            digital_num_obj = DigitalNumber()
            digital_number = [num_block[start_horizontal:start_horizontal + NUMBER_SIZE]
                              for num_block in data[start_vertical:start_vertical + NUMBER_SIZE]]
            number = digital_num_obj.digital2num(digital_number)
            if number == None:
                varients_of_number = recover_none_num(digital_num_obj, digital_number)
                flag_none_in_line = True
            else:
                varients_of_number.append(number)
            num_seq.append(varients_of_number)
            start_horizontal += NUMBER_SIZE + INDENT_SIZE
        parsed_num_list = list(product(*num_seq))
        num_list.append(processing_line(parsed_num_list, flag_none_in_line))
        start_vertical += NUMBER_SIZE + INDENT_SIZE
    return num_list


def get_parsing_result(data):
    parsed_num_list = convert_data_to_num_list(data)
    return parsed_num_list


def convert_digital_nums():
    arg_parser = argparse.ArgumentParser(description='Coverter digital numbers from file to usual numbers')
    arg_parser.add_argument('-i', '--input',  default=None, help='input filename for reading')
    arg_parser.add_argument('-o', '--output', default=None, help='output filename for writing')
    args = arg_parser.parse_args()
    if args.input:
        data = read_from_file(args.input)
    else:
        data = read_from_terminal()
    result_num_list = get_parsing_result(data)
    if args.output:
        write_to_file(result_num_list, args.output)
    else:
        write_to_terminal(result_num_list)


if __name__ == "__main__":
   convert_digital_nums()