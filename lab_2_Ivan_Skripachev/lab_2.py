import os
import sys
import copy
import argparse
from itertools import product

NUM_LINES_IN_DIGIT = 4
NUM_DIGITS = 9
DIGIT_WIDTH = 3
WEIGHT_COEF = 11

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-i', action='store', dest='input_file',  help='Path to file with input digits')
parser.add_argument('-o', action='store', dest='output_file', help='Path to file for result')
args = parser.parse_args()

digits_dict = {' _ | ||_|   ': '0',
               '     |  |   ': '1',
               ' _  _||_    ': '2',
               ' _  _| _|   ': '3',
               '   |_|  |   ': '4',
               ' _ |_  _|   ': '5',
               ' _ |_ |_|   ': '6',
               ' _   |  |   ': '7',
               ' _ |_||_|   ': '8',
               ' _ |_| _|   ': '9'}


def read_console():
    result = []
    for line in sys.stdin:
        result.append(line)
    if len(result) % NUM_LINES_IN_DIGIT != 0:
        raise SystemError('Incorrect number of lines in console')
    return result

def write_console(codes):
    for code in codes:
        print(code)


def read_file(file_name):
    if not os.path.exists(file_name):
        raise NameError('File not exist: ' + file_name)

    with open(file_name, 'r') as f:
        file_data = f.readlines()
        
        if len(file_data) % NUM_LINES_IN_DIGIT != 0:
            raise SystemError('Incorrect number of lines in file')

    return file_data


def write_file(file_name, data):
    with open(file_name, 'w') as f:
        for row in data:
            f.write(row + '\n')


def convert_digits(raw_digits_list):
    result = []
    was_recovered = False

    for digit in raw_digits_list:
        key = ('').join(digit)
        if key in digits_dict:
            digit = [digits_dict[key]]
        else:
            digit = recovery_digit(digit)
            was_recovered = True
        result.append(digit)
    
    result = list(product(*result))
    for i in range(len(result)):
        result[i] = ('').join(result[i]) + calc_status(result[i], was_recovered)
    
    return result


def recovery_digit(digit):
    result = []
    posHorizontalLine = [1, 4, 7]
    posVerticalLine = [3, 5, 6, 8]
    
    for i in posHorizontalLine:
        rec_digit = copy.copy(digit)
        rec_digit[i] = '_'
        rec_digit = ('').join(rec_digit)
        if rec_digit in digits_dict:
            result += digits_dict[rec_digit]
   
    for i in posVerticalLine:
        rec_digit = copy.copy(digit)
        rec_digit[i] = '|'
        rec_digit = ('').join(rec_digit)
        if rec_digit in digits_dict:
            result += digits_dict[rec_digit]
    
    if not result:
        return ['?']
    
    return result


def calc_status(code, was_recovered):
    if '?' in code:
        return ' ILL'
    
    weight_sum = 0
    for i in range(len(code)):
        weight_sum += int(code[i]) * (len(code) - i)

    if (weight_sum % WEIGHT_COEF) != 0:
        return ' ERROR'
    elif was_recovered:
        return ' RECOVERED'
    else:
        return ''


def procces_file_data(file_data):
    result = []

    for digit_line_idx in range(len(file_data) / NUM_LINES_IN_DIGIT):
        values = [[] for i in range(NUM_DIGITS)]
        for row_idx in range(NUM_LINES_IN_DIGIT):
            row_data = file_data[digit_line_idx * NUM_LINES_IN_DIGIT + row_idx].rstrip('\r\n')
            for i, col_idx in enumerate(range(0, len(row_data), DIGIT_WIDTH+1)):
                values[i] += row_data[col_idx:col_idx+DIGIT_WIDTH]
        
        conv_digit = convert_digits(values)
        for digit in conv_digit:
            result.append(digit)
    
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
        write_console(res)
    
if __name__ == '__main__':
    main()