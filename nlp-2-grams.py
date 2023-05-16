import re
import os
import csv
import nltk
from collections import Counter
from nltk import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from datetime import datetime
stop_words = set(stopwords.words('english'))

sentence = """1. This Agreement shall be open for signature and subject to ratification, acceptance or approval by States and regional economic integration organizations that are Parties to the Convention. It shall be open for signature at the United Nations Headquarters in New York from 22 April 2016 to 21 April 2017. Thereafter, this Agreement shall be open for accession from the day following the date on which it is closed for signature. Instruments of ratification, acceptance, approval or accession shall be deposited with the Depositary. 2. Any regional economic integration organization that becomes a Party to this Agreement without any of its member States being a Party shall be bound by all the obligations under this Agreement. In the case of regional economic integration organizations with one or more member States that are Parties to this Agreement, the organization and its member States shall decide on their respective responsibilities for the performance of their obligations under this Agreement. In such cases, the organization and the member States shall not be entitled to exercise rights under this Agreement concurrently."""

in_directory = '/Users/elchoco/clients/oldrich/files/input/small_set'
out_directory = '/Users/elchoco/clients/oldrich/files/csv/output/'
tag = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

n = 2


def single_file():
    txt_lower = sentence.lower() # lower case the document
    pattern = r'[^a-zA-Z\s]|\d+'
    txt_lower = re.sub(pattern, '', txt_lower)

    twograms = ngrams(txt_lower.split(), n)
    twoeuros = list(twograms)

    twofreq = Counter(twoeuros)

    with open(out_directory+tag+"_test"+".csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Frequency'])
        for word, freq in twofreq.most_common():
            mystring = ' '.join(word)
            writer.writerow([mystring,freq])

def multiple_files():
    for filename in os.listdir(in_directory):
        if filename.endswith('.txt'):
            with open(in_directory+'/'+filename, 'r') as infile:
                txt = infile.read()
                txt_lower = txt.lower() # lower case the document
                len(txt_lower)

                pattern = r'[^a-zA-Z\s]|\d+'
                txt_lower = re.sub(pattern, '', txt_lower)

                # twograms = ngrams(wordsList.split(), n)
                twograms = ngrams(txt_lower.split(), n)

                twoeuros = list(twograms)
                
                # frequency
                twofreq = Counter(twoeuros)
                
                with open(out_directory+tag+"_"+filename+".csv", 'w', newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(['Word', 'Frequency'])
                            for word, freq in twofreq.most_common():
                                mystring = ' '.join(word)
                                writer.writerow([mystring,freq])

if __name__ == "__main__":
    # single_file()
    multiple_files()