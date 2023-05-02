from collections import Counter
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))

with open('sample.txt', 'r') as infile:
	txt = infile.read()

	txt_lower = txt.lower() # lower case the document

	tokenized = sent_tokenize(txt_lower)
	nouns = []
	remove_words = ['fccc/cp/2015/10/add.1','fccc/cp/2015/7','fccc/sb/2015/inf.3','a','b','c','d','e','f','g','h','i','ii','iii','iv','v','vi','vii','a/res/70/1','’','“','”','>','<']
	
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
			if pos.startswith('N'):
				nouns.append(word)

		# outfile.write(' '.join(nouns))

	# 2nd step: sort
	# nouns.sort()

	# 3rd step: get frequency
	word_freq = Counter(nouns)
	
	# 4th step: cleanup process
	for word in remove_words:
		del word_freq[word]

	print(word_freq)
	print(len(nouns)) # 5515 nouns
	print(len(word_freq)) # 876 nouns
		# print(len(nouns))
