import csv

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
            keyword = row[0]

            with open('UNParis_A.txt', 'r') as file:
                count = 0
                for line in file:
                    count += line.count(keyword)
        
            print(f"The keyword '{keyword}' appears {count} times in the file.")
            print()