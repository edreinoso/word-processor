import re

list_of_words = ['This', 'document', 'introduction']

# function to convert Roman numeral to decimal
def roman_to_decimal(roman_num):
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    decimal_num = 0
    for i in range(len(roman_num)):
        if i > 0 and roman_dict[roman_num[i]] > roman_dict[roman_num[i-1]]:
            decimal_num += roman_dict[roman_num[i]] - 2 * roman_dict[roman_num[i-1]]
        else:
            decimal_num += roman_dict[roman_num[i]]
    return decimal_num

# read text file line by line
with open('./files/UNParis_A.txt', 'r') as f:
    current_section = None
    finished_section = False
    absolute_count = 0
    relative_count = 0

    for line in f:
        # check if line contains a Roman numeral
        roman_num_match = re.search('[IVXLCDM]+', line)
        # print(roman_num_match)
        if roman_num_match:
            # convert Roman numeral to decimal and update current section
            roman_num = roman_num_match.group(0)
            decimal_num = roman_to_decimal(roman_num)
            current_section = decimal_num
            # I want to be able to output the computation that happened below
            print('🚧 New section')
            
            
            # and then reset the counters, cause this is just bunch of counters
            absolute_count = 0
            relative_count = 0
        else:
            # compute something based on current section and current line
            if current_section is not None:
                # do computation here based on current_section and current line
                # mainly I would like to have the relative word count and the absolute word count
                print(f"Section {current_section}: {line}")
