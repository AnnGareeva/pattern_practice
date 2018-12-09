import os
import argparse

MAX_LEN_LINE = 39
NUM_LINES_IN_DIGIT = 4
MAX_NUM_DIGITS = 10
DIGIT_WIDTH = 3

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-i', action='store', dest='input_file',  help='Path to file with input digits')
parser.add_argument('-o', action='store', dest='output_file', help='Path to file for result')
args = parser.parse_args()

digits_dict = {'._.|.||_|...': '0',
               '.....|..|...': '1',
               '._.._||_....': '2',
               '._.._|._|...': '3',
               '...|_|..|...': '4',
               '._.|_.._|...': '5',
               '._.|_.|_|...': '6',
               '._...|..|...': '7',
               '._.|_||_|...': '8',
               '._.|_|._|...': '9'}


def read_console():
    result = []
    
    stop_input = False
    while True:
        for i in range(NUM_LINES_IN_DIGIT):
            input_data = raw_input()
            if len(input_data) > MAX_LEN_LINE:
                raise SystemError('Incorrect input')
            elif len(input_data) < MAX_LEN_LINE:
                stop_input = True
            result.append(input_data)
        if stop_input:
            break
    
    return result


def read_file(file_name):
    if not os.path.exists(file_name):
        raise NameError('File not exist: ' + file_name)

    with open(file_name, 'r') as f:
        file_data = f.readlines()
        
        if len(file_data) % NUM_LINES_IN_DIGIT != 0:
            raise SystemError('Incorrect file')

        for line in file_data:
            if len(line.rstrip()) > MAX_LEN_LINE:
                raise SystemError('Incorrect file')

    return file_data


def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.writelines(data)


def convert_digits(raw_digits_list):
    result = ''

    for digit in raw_digits_list:
        if digit:
            key = ('').join(digit)
            if key not in digits_dict:
                raise KeyError('Incorrect symbols in input digits')
            result += digits_dict[key]

    return result


def procces_file_data(file_data):
    result = ''

    for digit_line_idx in range(0, len(file_data) / NUM_LINES_IN_DIGIT):
        values = [[] for i in range(MAX_NUM_DIGITS)]
        for row_idx in range(NUM_LINES_IN_DIGIT):
            s = file_data[digit_line_idx * NUM_LINES_IN_DIGIT + row_idx].rstrip()
            for i, col_idx in enumerate(range(0, len(s), DIGIT_WIDTH+1)):
                values[i] += s[col_idx:col_idx+DIGIT_WIDTH]
        
        conv_digit = convert_digits(values)
        result += conv_digit

        if len(conv_digit) < MAX_NUM_DIGITS:
            break
    
    return result

def main():
    if args.input_file:
        file_data = read_file(args.input_file)
    else:
        file_data = read_console()

    res = procces_file_data(file_data)

    if args.output_file:
        write_file(args.output_file, res)
    else:
        print(res)
    
if __name__ == '__main__':
    main()