CHAR_TO_INT_DICT = {
                    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, 
                    "G": 16, "H": 17, "I": 18, "J": 19, "K": 20, "L": 21,
                    "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27,
                    "S": 28, "T": 29, "U": 30, "V": 31, "W": 32, "X": 33,
                    "Y": 34, "Z": 35,
                    }

INT_TO_CHAR_DICT = {
                    10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F",
                    16: "G", 17: "H", 18: "I", 19: "J", 20: "K", 21: "L",
                    22: "M", 23: "N", 24: "O", 25: "P", 26: "Q", 27: "R", 
                    28: "S", 29: "T", 30: "U", 31: "V", 32: "W", 33: "X", 
                    34: "Y", 35: "Z",
                    }

#  If you can use built-in functions, use int(number, system_of_number)
def change_number_system_to_decimal(string_of_number: str, base: int): 
    string_of_number = string_of_number.upper()  # unify number eg.Ac3 -> AC3
    # change "AC13" into [10, 12, 1, 3]    
    digitized_number = digitize_number(string_of_number)  
    decimal_value = 0

    for int_of_char in digitized_number:
        decimal_value *= base
        decimal_value += int_of_char

    return decimal_value

# change "abc123" into [10, 11, 12, 1, 2, 3]
def digitize_number(string_of_number: str):  
    digitized_number = [None] * len(string_of_number)
    for idx, chr in enumerate(string_of_number):
        try:    
            digitized_number[idx] = int(chr)
        except ValueError:
            digitized_number[idx] = CHAR_TO_INT_DICT[chr]
    return digitized_number

def compress_number_to_string_number(array_of_number):
    compressed_number = ""
    for idx, chr in enumerate(array_of_number):
        if chr < 10:
            compressed_number += str(chr)
        else:
            compressed_number += INT_TO_CHAR_DICT[chr]
    return compressed_number

def change_number_to_another_system(number_in_decimal: int, target_base: int):
    new_number_digits = []
    while number_in_decimal >= target_base:
        new_number_digits.append(number_in_decimal % target_base)
        number_in_decimal //= target_base 
    new_number_digits.append(number_in_decimal)
    new_number = compress_number_to_string_number(new_number_digits)[::-1]
    return new_number


#  Sample usage:

string_of_number = input("First number: ")  # abc123 or ABC123
base_system = int(input("Number system (2 <= int <= 36): "))  #   16
target_system = int(input("Target number system (2 <= int <= 36): "))  # 17

number_in_decimal = change_number_system_to_decimal(string_of_number, base_system)
number_in_new_system = change_number_to_another_system(number_in_decimal, target_system)
