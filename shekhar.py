from matplotlib import pyplot
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from numpy import dot
from numpy.linalg import norm


def welcome_message():
    print("------------------Success to Oldrich-------------------")


def prepare_data_from_csv(file):
    # We only focus on first three columns - keyword, frequency in UN, frequency in Company_Year (others not relevant)
    # sorting of data in csv is not important, otherwise the graph would look falling horizontally as it progresses
    df = pd.read_csv(file, sep=',')
    df = df[(df['Found_In_UN'] == 1) & (df['Found_In_Shell2012'] == 1)]
    un = df['Frequency_UN']
    shell_2012 = df['Frequency_Shell_2012']
    bins = df.index.values
    print(un)
    print(shell_2012)
    # print(type(bins))
    labels = np.arange(len(bins))
    ticks = [un, shell_2012]
    fig, axes = pyplot.subplots()
    axes.bar(labels, list(map(int, ticks[0])), align='edge', label='United Nations', width=-0.1)
    pyplot.xticks(labels)
    # axes.set_xticklabels(bars, rotation='horizontal')
    axes.bar(labels, list(map(int, ticks[1])), align='edge', label='Shell 2012', width=0.1)

    pyplot.legend(loc='upper right')
    pyplot.title("Plot comparing keyword frequencies between \n the company and UN for the year 2012")
    pyplot.xlabel("Keywords that are common in UN and the Company")
    pyplot.ylabel("Keyword-frequency")
    pyplot.show()
    fig.savefig('Shell-2012_UN_influence_analysis.png', bbox_inches='tight')
    # chi_squared_influence_analysis(shell_2012, un)
    cosine_similarity(shell_2012, un)


def cosine_similarity(list_a, list_b):
    cos_sim = dot(list_a, list_b) / (norm(list_a) * norm(list_b))
    print(f"Cos-similarity = {cos_sim}")


def chi_squared_influence_analysis(company_year_word_frequency, un_word_frequency):
    # src - https://www.askpython.com/python/examples/chi-square-test
    print(type(company_year_word_frequency.to_numpy()))
    print(type(un_word_frequency.to_numpy()))
    info = [company_year_word_frequency.to_numpy(), un_word_frequency.to_numpy()]
    print(info)
    stat, p, dof = chi2_contingency(info)
    print(dof)
    # The null hypothesis: The grouping variables have no association or correlation amongst them.
    # The alternate Hypothesis: The variables are associated with each other and happen to have a correlation between the variables.
    significance_level = 0.05
    print("p value: " + str(p))
    if p <= significance_level:
        print('Reject NULL HYPOTHESIS')
    else:
        print('ACCEPT NULL HYPOTHESIS')
    # If the p-value is less than the assumed significance value (0.05), then we fail to accept that there is
    # no association between the variables: we reject the NULL hypothesis, else, we accept the alternate hypothesis claim.


if __name__ == '__main__':
    welcome_message()
    file = 'shekhar_sample_data.csv'
    prepare_data_from_csv(file)
