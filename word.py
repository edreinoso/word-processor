import csv
import re

with open('copy2_overlap.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Get the header row and store it in a variable
    header = next(csvreader)

    print(header)
    print()
    
    # Iterate over the remaining rows in the CSV file
    for row in csvreader:
        """
         If the last and second to last index of the row match
            Bingo, there needs to be some computation
                here needs to 
        """
        if (row[3] == '1'):
            print('bingo for word', row[0])
            
            with open('UNParis_A.txt', 'r') as file:
                keyword = row[0]
                count = 0
                locations = []

                for line_num, line in enumerate(file, start=1):
                    for match in re.finditer(keyword, line):
                        count += 1
                        location = (line_num, match.start())
                        locations.append(location)
                        
                print(f"The keyword '{keyword}' appears {count} times in the file at the following locations:")
                for location in locations:
                    print(f"Line {location[0]}, position {location[1]}")
                print()