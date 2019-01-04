import operator
import argparse

class Converter:
    _roman_symbols = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}

    def _valid_roman_value(self, roman_num):
        if not isinstance(roman_num, str):
            raise TypeError('The passed value is not string')

        result = roman_num.lower()
        
        for symbol in result:
            if symbol not in Converter._roman_symbols:
                raise ValueError('The passed value has not Roman symbols')
        return result

    
    def _valid_arab_value(self, arab_num):
        try:
            arab_num = int(arab_num)
        except:
            raise ValueError('Invalid input value')
        if arab_num > 0:
            if arab_num > 3000:
                raise ValueError('Input value must be < 3000')
            else:
                return True
        else:
            raise ValueError('Input value must be > 0')
    

    def arab_to_roman(self, arab_num):
        dict_roman = sorted(Converter._roman_symbols, key=Converter._roman_symbols.get, reverse=True)
        dict_roman = {roman_symb:Converter._roman_symbols[roman_symb] for roman_symb in dict_roman}

        if self._valid_arab_value(arab_num):
            self.arab_value = arab_num
            roman_num = ''
            rom_symb = list(dict_roman.keys())
            idx = 0
            step_idx = 2
            while arab_num > 0:
                current_idx = idx * step_idx
                count = (arab_num // dict_roman[rom_symb[current_idx]]) 
                if idx > 0:
                    fives = arab_num // dict_roman[rom_symb[current_idx - 1]]
                    ones = count - fives * 5
                    if ones < 4 and fives > 0:
                        combination = str(rom_symb[current_idx - 1] * fives
                                        + rom_symb[current_idx]     * ones)
                    elif ones == 4 and fives > 0:
                        combination = str(rom_symb[current_idx] 
                                        + rom_symb[current_idx - step_idx])
                    elif ones == 4 and fives == 0:
                        combination = str(rom_symb[current_idx] 
                                        + rom_symb[current_idx - 1])
                    else:
                        ones = (arab_num // dict_roman[rom_symb[current_idx]])
                        combination = rom_symb[current_idx] * ones
                else:
                    ones = (arab_num // dict_roman[rom_symb[current_idx]])
                    combination = rom_symb[current_idx] * ones

                roman_num += combination
                arab_num -= count * dict_roman[rom_symb[current_idx]]
                idx += 1
                        
        self.roman_value = roman_num
        return self.roman_value.upper()


    def roman_to_arab(self, roman_num):
        lower_case_num = self._valid_roman_value(roman_num)
        list_arab_nums = list(map(lambda x: Converter._roman_symbols[x], lower_case_num))

        result = 0
        while True:
            max_val_idx = list_arab_nums.index(max(list_arab_nums))
            if list_arab_nums[max_val_idx] == -1:
                break
            result += list_arab_nums[max_val_idx]
            list_arab_nums[max_val_idx] = -1
            prev_val_idx = max_val_idx - 1
            if prev_val_idx >= 0 and list_arab_nums[prev_val_idx] != -1:
                result -= list_arab_nums[prev_val_idx]
                list_arab_nums[prev_val_idx] = -1
        
        if result > 3000:
            raise OverflowError('Roman value should be less then 3000')
        
        return result



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', required=True, help='input arabic number')
    args = parser.parse_args()
    num = int(args.i)
    print(Converter().arab_to_roman(num))