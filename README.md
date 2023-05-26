# Word Processor
**Determining the Linguistic Influence of the Fossil Fuel Industry on the Post-Paris Interantional Climate Regime Through Content, Frame and Discourse Analyses.**

## General
In this repository, different modules are used for analyzing and processing a number of documents with the goal of finding common patterns. The structure of the directories is as follow:

*/root*: there are two primary files:

- **npl-word-counter.py**: is responsible for counting the number of words, their frequency and the absolute value in terms of how many times it appears in the document.
- **word.py**: is responsible for highlighting the output words in the documents that were analyzed.

*/files*: location where input and output files reside.
- **Input**: 170 documents from different companies and organizations.
- **Output**: 340 csv files with nouns and 2 gram words from those documents.

## Natural Language Processing

This part of the document processing was done using nltk, a python librabry suitable for analyzing text documents.

https://www.nltk.org/

The logic then was split for analyzing the nouns and the two grams in a document.


For nouns
1. Used nltk library to tokenise the corpus and filter all the nouns and proper nouns 
2. Filtred punctuation and numbers
3. Lowercase
4. Sort with relative and total frequency
5. Generate csv

2euros 
Not sure if we tokenise something and if we used some stop-words
1. Lowercase 
2. Filter all punctuation and numbers
3. Split to 2-grams (maybe a better word for it)
4. Sort and count 
5. Export to csv