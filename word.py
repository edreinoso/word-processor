import csv
import os

in_directory = '/Users/elchoco/clients/oldrich/files'
temp_file = "file.txt"

paris_agreement_path = '/Users/elchoco/clients/oldrich/files/PA.txt'
paris_rulebook_path = '/Users/elchoco/clients/oldrich/files/PR.txt'
glasgow_climate_path = '/Users/elchoco/clients/oldrich/files/GCP.txt'

with open(paris_agreement_path, 'r') as file:
    paris_agreement_text = file.read()
with open(paris_rulebook_path, 'r') as file:
    paris_rulebook_text = file.read()
with open(glasgow_climate_path, 'r') as file:
    glasgow_climate_text = file.read()

def insert_emojis(text, word, frequency, emoji):
    modified_text = text.replace(word, emoji + '-' + frequency + '-' + word + '-' + frequency + '-' + emoji)
    return modified_text

def main():
    pa_emoji = paris_agreement_text
    pr_emoji = paris_rulebook_text
    gcp_emoji = glasgow_climate_text
    for filename in os.listdir(in_directory):
	    if filename.endswith('.csv'):
                with open(in_directory+'/'+filename, 'r') as file:
                    reader = csv.reader(file)
                    matrix = []

                    for row in reader: 
                        matrix.append(row) # creating a matrix
                    
                    # Iterate through columns first, then rows
                    for j in range(1,len(matrix[0])):
                        doc_name = matrix[0][j].split(" ")[1]
                        # print('###',doc_name)
                        """if doc_name == 'PA':
                            main_text = paris_agreement_text
                        elif doc_name == 'PR':
                            main_text = paris_rulebook_text
                        else:
                            main_text = glasgow_climate_text"""
                        
                        for i in range(1,len(matrix)):
                            word = matrix[i][0]
                            frequency = matrix[i][1]
                            
                            if filename == 'sheet1.csv':
                                emoji = '🛑'
                            else: 
                                emoji = '🟢'
                            
                            # main_text = insert_emojis(main_text, word, frequency, emoji)
                            if doc_name == 'PA':
                                pa_emoji = insert_emojis(pa_emoji, word, frequency, emoji)
                            elif doc_name == 'PR':
                                pr_emoji =  insert_emojis(pr_emoji, word, frequency, emoji)
                            else:
                                gcp_emoji = insert_emojis(gcp_emoji, word, frequency, emoji)

    # Write the main_text into a file
    with open(in_directory+'/out/pa.txt', 'w') as output_file:
        output_file.write(pa_emoji)
    with open(in_directory+'/out/pr.txt', 'w') as output_file:
        output_file.write(pr_emoji)
    with open(in_directory+'/out/gcp.txt', 'w') as output_file:
        output_file.write(gcp_emoji)

if __name__ == "__main__":
    main()