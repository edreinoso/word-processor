# word-similarity-analyser
The purpose of this application/project is to calculate the cosine similarity of lists of words, and plot them for each 
company provided in the source file, and then plot their cosine similarity with respect to their presence in the document
for each year.

The input data consists of a workbook (or, an Excel workbook with multiple sheets) file which consists of various sheets
consisting of 1-gram (unigram) and 2-gram (bigram) words pertaining to the UN policy document and various companies' 
policy document for different years.

They are correlated based on the common keywords with respect to various UN policy documents, one at a time. The method 
of similarity calculation used in our case is cosine-similarity calculation (based on an idea somewhat similar to the 
one used in the literature "The Implementation of Cosine Similarity to Calculate Text Relevance between Two Documents" - 
https://iopscience.iop.org/article/10.1088/1742-6596/978/1/012120/pdf).

Once we have the cosine similarity of the company's policy document for each year with respect to the UN policy document,
we plot the cosine similarity score for both absolute frequency and relative frequency of the common unigrams and bigrams
for each year for each company. The closer the cosine-similarity value is to 1, the documents can be said to be more 
closely related.

In our technical implementation of the basic idea presented above, we have used a Python application consisting of two 
Python files for reaching the analysis, namely:
(i) final_version.py, and (ii) plotting.py. Both these files jointly serve as a common application to achieve the desired 
analysis result.

- final_version.py: This Python program reads a workbook (or, an Excel workbook with multiple sheets) consisting of 
various sheets having either a 1-gram or a 2-gram analysis of a company's policy document and a UN policy document for 
a specific agreement year. The goal is to find common words which can be compared and merged, and both the former (the 
company) and the latter (UN)'s total and relative frequency is calculated (in `prepare_data_from_excel()` function) 
for cosine similarity analysis (in `cosine_similarity()` function). This program also calculates and stores the common 
word for each pair, mainly considering common words from UN specific agreement as the source (each sheet corresponds to 
words from a specific UN agreement document), which is done in `common_data_from_excel()` function. The execution of the
program starts from `main()` function, performing the operations successively as explained.


- plotting.py: This Python program reads the CSV files as input which consists of company-name, document-year, 
cosine-similarity calculated on total frequency of common words (with respect to UN document for each agreement), and
cosine-similarity calculated on relative frequency of common words (with respect to UN document for each agreement). 
These are plotted for total-frequency and relative-frequency for each company for each UN agreement document (in 
`prepare_data_from_csv_to_plot()` function). The execution of the program starts from `main()` function, performing the 
operations successively as explained.
