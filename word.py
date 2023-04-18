import csv
import re
import os

temp_file = 'temp.txt'

document_dict = {
    'paris': 'UNParis_A.txt',
    'bp':'BP_2015.txt',
    'shell':'Shell_2015.txt'
}

def process_file(word, file_name):
    """ 
        Reading the file 
            the UN file always have to be read and analyzed

    """
    print(word, file_name)
    # I should also append the word to a list
    # if the word has already been marked for UN
    # do not do anything
    # with open('UNParis_A.txt', 'r') as file:
    #     count = 0
    #     locations = []

    #     for line_num, line in enumerate(file, start=1):
    #         for match in re.finditer(word, line):
    #             count += 1
    #             location = (line_num, match.start())
    #             locations.append(location)
                
    #     # print(f"The word '{word}' appears {count} times in the file")
    #     print(f"The word '{word}' appears {count} times in the file at the following locations:")
    #     # for location in locations:
    #         # print(location)
    #         # print(f"Line {location[0]}, position {location[1]}")
        
    # """ Modify the File """
    # with open('UNParis_A.txt', 'r') as file:
    #     modified_word = '🛑' + word + '🛑'

    #     with open(temp_file, 'w') as temp:
            
    #         for line_num, line in enumerate(file, start=1):
    #             for location in locations:
    #                 if location[0] == line_num:
    #                     start_pos = location[1]
    #                     end_pos = start_pos + len(word)
    #                     line = line[:start_pos] + modified_word + line[end_pos:]
    #             temp.write(line)

    # os.replace(temp_file, 'UNParis_A.txt')

def main():
    counter = 0

    with open('copy2_overlap.csv', 'r') as file:
        reader = csv.reader(file)
        matrix = []
        for row in reader: 
            matrix.append(row) # creating a matrix

        # Iterate through columns first, then rows
        for j in range(3,len(matrix[0])):
            print('----col', matrix[0][j]) # sanity check
            
            file_name = matrix[0][j].split("_")[-1]

            for i in range(1,len(matrix)):
                word = matrix[i][0]
                # print('i:',i,'word:',matrix[i][0])
                if matrix[i][j] == '1':
                    # print('match',matrix[i][j])
                    process_file(word, file_name)
    # with open('copy2_overlap.csv', 'r') as file:
    #     reader = csv.reader(file)
        
    #     header = next(reader)

    #     n = 3

    #     new_list = header[n:]

    #     # print(new_list)

    #     for cols in new_list:
    #         print(cols)
    #         for row in reader:
    #             print(row)
        
    #     # for row in reader:
    #     #     for col in row:
    #     #         print(col)
    
    # with open('copy2_overlap.csv', 'r') as csvfile:
    #     csvreader = csv.reader(csvfile)
        
    #     # Get the header row and store it in a variable
        
    #     header = next(csvreader)

    #     n = 3

    #     new_list = header[n:]

    #     for columns in new_list:
    #         counter += 1
    #         print(columns)
    #         # Iterate over the remaining rows in the CSV file
    #         for row in csvreader:
    #             # the first row would pertain the name
    #         #     """ If comparison """
    #         #     """ 
    #         #         you should be able to get the name of the the column
    #         #         trim the string to the last _, so that you know which
    #         #         document you're going to be manipulating
    #         #     """
    #             # if (row[2+counter] == '1'): # UN_Overlap_Shell
    #             print(2+counter)
    #             # print(row[2+counter])
    #         #     # if (row[3] == '1'): # UN_Overlap_Shell
    #         #         # print('bingo for word', row[0])
    #         #         # process_file(row[0])
    #         #         print()
        
    #     # print(header)
    #     # print()
        
if __name__ == "__main__":
    main()


    
    
    """Do this for the Shell document"""