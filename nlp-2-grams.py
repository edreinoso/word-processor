import re
import nltk
from collections import Counter
from nltk import ngrams
from nltk.corpus import stopwords
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

n = 2

wordsList = [ w for w in sentence if not w in stop_words ]

# Using a Tagger. Which is part-of-speech
# tagger or POS-tagger.
tagged = nltk.pos_tag(wordsList)

twograms = ngrams(sentence.split(), n)

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
# print(cleaned_list_nested)

# print(twoeuros)

# frequency
twofreq = Counter(cleaned_list_nested)
# twofreq = Counter(twoeuros)

print(twofreq)

# for grams in sixgrams:
#   print(grams, type(grams))