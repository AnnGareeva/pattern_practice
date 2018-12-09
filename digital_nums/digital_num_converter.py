import argparse
import itertools
import os

__all__ = ['convert_digital_nums']


class DigitalNumber:
    matching_num_dict = {'0': [True, True, True, True, True, False, True],
                         '1': [False, False, True, True, False, False, False],
                         '2': [False, True, True, False, True, True, True],
                         '3': [False, False, True, True, True, True, True],
                         '4': [True, False, True, True, False, True, False],
                         '5': [True, False, False, True, True, True, True],
                         '6': [True, True, False, True, True, True, True],
                         '7': [False, False, True, True, True, False, False],
                         '8': [True, True, True, True, True, True, True],
                         '9': [True, False, True, True, True, True, True]}

    def __init__(self):
        self.left_up = False
        self.left_down = False
        self.right_up = False
        self.right_down = False
        self.center_up = False
        self.center_middle = False
        self.center_down = False
        self.number = None

    def convert_to_num(self):
        position_list = [self.left_up,
                         self.left_down,
                         self.right_up,
                         self.right_down,
                         self.center_up,
                         self.center_middle,
                         self.center_down]
        for key, value in self.matching_num_dict.items():
            if value == position_list:
                res_number = int(key)
                self.number = res_number

    def digital2num(self, digital_num_str):
        horiz_line = '_'
        vert_line = '|'
        self.left_up = True if vert_line == digital_num_str[1][0] else False
        self.left_down = True if vert_line == digital_num_str[2][0] else False
        self.right_up = True if vert_line == digital_num_str[1][2] else False
        self.right_down = True if vert_line == digital_num_str[2][2] else False
        self.center_up = True if horiz_line in digital_num_str[0] else False
        self.center_middle = True if horiz_line in digital_num_str[1] else False
        self.center_down = True if horiz_line in digital_num_str[2] else False
        self.convert_to_num()
        return self.number


def convert_data_to_num_list(digital_num_obj, data):
    start_vertical = 0
    num_size_horizontal = 3
    num_size_vertical = 3
    stop_counter = 9
    num_list = []
    while start_vertical < len(data) - num_size_vertical + 1:
        start_horizontal = 0
        counter = 0
        num_str = []
        while start_horizontal < len(data[start_vertical]) - num_size_horizontal + 1:
            digital_number = [num_block[start_horizontal:start_horizontal + num_size_horizontal]
                              for num_block in data[start_vertical:start_vertical + num_size_vertical]]
            number = digital_num_obj.digital2num(digital_number)
            if not number:
                raise Exception('Invalid combination of symbols. Number is not found')
            num_str.append(number)
            start_horizontal += num_size_horizontal + 1
            counter += 1
        num_list.append(num_str)
        start_vertical += num_size_vertical + 1
        if counter < stop_counter:
            break
    return num_list


def check_valid_size(line):
    number_size = 4
    if len(line) % number_size != 0 and len(line) % number_size != 3:
        raise Exception('Not valid size of data. Size of one digital number 4x4 symbols')
    return line


def check_valid_symbols(data):
    valid_symb = ['\n', '\t', ' ', '|', '_', '.']
    for string in data:
        for el in string:
            if not el in valid_symb:
                raise Exception('Invalid symbol {symb} in source data'.format(symb=el))


def read_from_file(filename):
    if not os.path.exists(filename):
        raise Exception('{filename} does not exist'.format(filename=filename))
    with open(filename, 'r') as input_file:
        data = input_file.readlines()
    check_valid_size(data)
    check_valid_symbols(data)
    for line in data:
        check_valid_size(line)
    return data


def read_num_line_terminal():
    list_line = [check_valid_size(input()) for i in range(4)]
    return list_line


def read_from_terminal():
    data = []
    min_counter = 9
    line = read_num_line_terminal()
    data.append(line)
    line_num_size = 4
    while len(line) / line_num_size >= min_counter:
        line = read_num_line_terminal()
        data.append(line)
    data = list(itertools.chain(*data))
    check_valid_symbols(data)
    return data


def write_to_file(list_num, filename):
    with open(filename, 'w') as f:
        for line in list_num:
            for num in line:
                f.write('{} '.format(num))
            f.write('\n')


def write_to_terminal(list_num):
    for line in list_num:
        for num in line:
            print('{}'.format(num), end=' ')
        print()


def convert_digital_nums():
    arg_parser = argparse.ArgumentParser(description='Coverter digital numbers from file to usual numbers')
    arg_parser.add_argument('-i', '--input', default=None, help='input filename for reading')
    arg_parser.add_argument('-o', '--output', default=None, help='output filename for writing')
    args = arg_parser.parse_args()

    if args.input:
        data = read_from_file(args.input)
    else:
        data = read_from_terminal()
    dn = DigitalNumber()
    result_list = convert_data_to_num_list(dn, data)
    if args.output:
        write_to_file(result_list, args.output)
    else:
        write_to_terminal(result_list)


if __name__ == "__main__":
   convert_digital_nums()