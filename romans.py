import re

list_of_words = ['Parties',
    'Agreement',
    'Article',
    'Conference']
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
with open('./files/UNParis_A_romans.txt', 'r') as f:
    current_section = None
    finished_section = False
    absolute_count = 0
    relative_count = 0
    total_num_words = 0

    while True:
        line = f.readline()
        
        if not line:
            print('🚧 Total num of words', total_num_words, '\nabsolute count (nouns)', absolute_count, 'relative count', relative_count)
            break

        # check if line contains a Roman numeral
        roman_num_match = re.search(r"\b[IVXLCDM]+\.", line)
        # roman_num_match = re.search('[IVXLCDM]+', line)
        # print(roman_num_match)
        # if roman_num_match:
            # roman_num = roman_num_match.group(0)
            # print('hello',roman_num)
        # else:
            # print('world')
        
        if roman_num_match:
            # convert Roman numeral to decimal and update current section
            roman_num = roman_num_match.group(0)
            # decimal_num = roman_to_decimal(roman_num)
            # current_section = decimal_num
            # I want to be able to output the computation that happened below
            if total_num_words != 0:
                relative_count = absolute_count / total_num_words
                print('🚧 Total num of words', total_num_words, '\nabsolute count (nouns)', absolute_count, 'relative count', relative_count)
            # print('🚧 New section')
            print(roman_num)
            # and then reset the counters, cause this is just bunch of counters
            absolute_count = 0
            relative_count = 0
            total_num_words = 0
        else:
            # compute something based on current section and current line
            # if current_section is not None:
            # do computation here based on current_section and current line
            # mainly I would like to have the relative word count and the absolute word count
            line_words = len(line.split())
            total_num_words += line_words
            for word in list_of_words:
                if word in line:
                    absolute_count += 1
            # print(f"Section {current_section}: {line} Word count {line_words}")
