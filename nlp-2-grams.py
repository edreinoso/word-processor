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

sentence = """The promotion of road safety awareness among
people in local communities is another focus
area of our social investment projects. In southern
Iraq, for example, near our Majnoon operations,
we work with the AMAR International Charitable
Foundation to train local health staff and women
safety volunteers to raise awareness among
parents and children about road safety. We
are also working with authorities in education,
government and the police to set up road safety
zones around primary schools and build speed
bumps, new footpaths and warning signs.
We are a board member of the Global Road
Safety Partnership (GRSP), a global alliance that
brings together governments, civil society and
businesses to improve road safety. Shell chairs
the Global Road Safety Initiative, a private sector
collaboration with GRSP that works to improve
road safety in cities and communities. It operates
in eight countries and its “Safe to School –
Safe to Home” programme focuses on helping
children to travel safely to and from school.
(See more on our road safety work on page 32)."""

in_directory = '/Users/elchoco/clients/oldrich/files/input/small_set'
out_directory = '/Users/elchoco/clients/oldrich/files/csv/output/'
tag = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

n = 2

for filename in os.listdir(in_directory):
    if filename.endswith('.txt'):
        with open(in_directory+'/'+filename, 'r') as infile:
            txt = infile.read()
            txt_lower = txt.lower() # lower case the document
            print(type(txt_lower))

            # tokenized = sent_tokenize(txt_lower)

            # for i in tokenized:
            # wordsList = nltk.word_tokenize(i)

            wordsList = [ w for w in txt_lower if not w in stop_words ]
            
            # print(type(wordsList))
            
            # Using a Tagger. Which is part-of-speech
            # tagger or POS-tagger.
            tagged = nltk.pos_tag(wordsList)
            
            # twograms = ngrams(wordsList.split(), n)
            twograms = ngrams(txt_lower.split(), n)

            twoeuros = list(twograms)
            
            # removing special characters
            # would probably have to test whether this may be accurate 
            pattern = r'[^\w\s]'
            cleaned_list_nested = []
            for tpl in twoeuros:
                cleaned_tpl = []
                for element in tpl:
                    cleaned_element = re.sub(pattern, '', element)
                    cleaned_tpl.append(cleaned_element)
                cleaned_list_nested.append(tuple(cleaned_tpl))
            # print(twoeuros)
            
            # frequency
            # twofreq = Counter(cleaned_list_nested)
            twofreq = Counter(twoeuros)
            # print(twofreq)
            
            with open(out_directory+tag+"_"+filename+".csv", 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(['Word', 'Frequency'])
                        for word, freq in twofreq.most_common():
                            mystring = ' '.join(word)
                            writer.writerow([mystring,freq])