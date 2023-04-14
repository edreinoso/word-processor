import csv
import re
import os

temp_file = 'temp.txt'

with open('copy2_overlap.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Get the header row and store it in a variable
    header = next(csvreader)

    print(header)
    print()
    
    # Iterate over the remaining rows in the CSV file
    for row in csvreader:
        """ If comparison """
        if (row[3] == '1'):
            print('bingo for word', row[0])
            
            # Do this for the UN document
            with open('UNParis_A.txt', 'r') as file:
                keyword = row[0]
                count = 0
                locations = []

                for line_num, line in enumerate(file, start=1):
                    for match in re.finditer(keyword, line):
                        count += 1
                        location = (line_num, match.start())
                        locations.append(location)
                        
                print(f"The keyword '{keyword}' appears {count} times in the file")
                # print(f"The keyword '{keyword}' appears {count} times in the file at the following locations:")
                # for location in locations:
                #     print(f"Line {location[0]}, position {location[1]}")
                print()

                """ Modify the File """
                modified_keyword = '🛑' + keyword + '🛑'

                with open(temp_file, 'w') as temp:
                    for line_num, line in enumerate(file, start=1):
                        for location in locations:
                            if location[0] == line_num:
                                start_pos = location[1]
                                end_pos = start_pos + len(keyword)
                                line = line[:start_pos] + modified_keyword + line[end_pos:]
                        temp.write(line)
            
            os.replace(temp_file, 'UNParis_A.txt')
            # Do this for the Shell document
    