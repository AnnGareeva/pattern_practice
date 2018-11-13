class Converter:
    _roman_symbols = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}

    def _valid_roman_value(self, roman_num):
        if not isinstance(roman_num, str):
            raise ValueError('The passed value is not string')

        result = roman_num.lower()
        
        for symbol in result:
            if symbol not in Converter._roman_symbols:
                raise ValueError('The passed value has not Roman symbols')
        return result
            
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
            raise ValueError('Roman value should be less then 3000')
        
        return result
