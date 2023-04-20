import csv
import re
import os

local_word_list = []

document_dict = {
    'paris': 'UNParis_A.txt',
    'bp':'BP_2015.txt',
    'shell':'Shell_2015.txt'
}

def process_file(word, frequency, file_name):
    value = document_dict[file_name.lower()]
    list_docs = [document_dict['paris'], value]
    # list_docs = [value]
    
    for docs in list_docs:
        if docs == 'UNParis_A.txt' and word in local_word_list:
            # print('*** word has already been added',docs,word, frequency, file_name)
            continue
        
        else:
            print('new word',docs,word, frequency, file_name)
            local_word_list.append(word)
            """ Reading from the file """
            with open(docs, 'r') as file:
                count = 0
                locations = []

                for line_num, line in enumerate(file, start=1):
                    for match in re.finditer(word, line):
                        count += 1
                        location = (line_num, match.start())
                        locations.append(location)
                        
                # print(f"The word '{word}' appears {count} times in the file")
                print(f"The word '{word}' appears {count} times in the file at the following locations:")
                # for location in locations:
                    # print(location)
                    # print(f"Line {location[0]}, position {location[1]}")
            
            """ Writing to the file """
            temp_file = 'temp.txt'
            with open(docs, 'r') as file: # I have to open the file again, otherwise there would be an error.
                modified_word = '🛑' + frequency + "-" + word + "-" + frequency + '🛑'
                with open(temp_file, 'w') as temp:
                    # # If I don't open the file again, there would not be any reading
                    for line_num, line in enumerate(file, start=1):
                        for location in locations:
                            if location[0] == line_num:
                                start_pos = location[1]
                                end_pos = start_pos + len(word)
                                line = line[:start_pos] + modified_word + line[end_pos:]
                        temp.write(line)
            os.replace(temp_file, docs)

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
                frequency = matrix[i][1]
                # print('i:',i,'word:',matrix[i][0])
                if matrix[i][j] == '1':
                    # print('match',matrix[i][j])
                    process_file(word, frequency, file_name)
            print()

if __name__ == "__main__":
    main()