from collections import Counter
import csv
import nltk
import os
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))

directory = '/Users/elchoco/clients/oldrich/files/input/small_set'

for filename in os.listdir(directory):
	if filename.endswith('.txt'):
		print(filename)

		with open(directory+'/'+filename, 'r') as infile:
			txt = infile.read()

			txt_lower = txt.lower() # lower case the document

			tokenized = sent_tokenize(txt_lower)
			nouns = []
			remove_words_in_un_docs = ['fccc/cp/2015/10/add.1','fccc/cp/2015/7','fccc/sb/2015/inf.3','vii','a/res/70/1']
			
			for i in tokenized:
				
				# Word tokenizers is used to find the words
				# and punctuation in a string
				wordsList = nltk.word_tokenize(i)

				# removing stop words from wordList
				wordsList = [ w for w in wordsList if not w in stop_words ]

				# Using a Tagger. Which is part-of-speech
				# tagger or POS-tagger.
				tagged = nltk.pos_tag(wordsList)

				# 1st step: tokenize
				for word, pos in tagged:
					# print(word, len(word))
					# if pos.startswith('N'):
					if pos.startswith('N') and len(word) > 2:
						# print(word, len(word))
						nouns.append(word)

				# outfile.write(' '.join(nouns))

			# 2nd step: get frequency
			word_freq = Counter(nouns)
			
			# 3rd step (optional): cleanup process
			"""
			This step should only be done for the UN documents
			"""
			if "UN" in filename:
				for word in remove_words_in_un_docs:
					del word_freq[word]

			# print(word_freq)
			print(len(nouns)) # 5515 nouns
			print(len(word_freq)) # 876 nouns

		with open(directory+'/'+filename+"out.csv", 'w', newline='') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(['Word', 'Frequency'])
			for word, freq in word_freq.most_common():
				# print(word, freq)
				writer.writerow([word,freq])