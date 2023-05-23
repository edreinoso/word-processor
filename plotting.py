import pandas as pd
from matplotlib import pyplot
import glob


def prepare_data_from_csv_to_plot(file):
    # This function is used to plot the overlap-score and cos-similarity value for different companies varying with year
    df = pd.read_csv(file, sep=',')
    # print(df)
    ##### TOTAL_FREQUENCY #####
    fig, ax = pyplot.subplots(figsize=(12, 4))
    # ax2 = ax.twinx()
    for key, grp in df.groupby(['Company']):
        l1, = ax.plot(grp['Year'], grp['Cosine-similarity_Total_Frequency'], label=key)
        # l2, = ax2.plot(grp['Year'], grp['Overlap-coefficient'], linestyle='dashed')
    ax.legend()
    pyplot.legend(loc='upper right')
    pyplot.title("Plot comparing keyword frequencies between \n the companies and UN")
    pyplot.xlabel("Publishing year of agreement document of the companies")
    pyplot.ylabel("Document's cosine-similarity of total frequencies")
    # ax2.set_ylabel('Overlap-coefficient', color='b')
    pyplot.show()
    fig.savefig('new-plots/'+file.lstrip('new-data/').rstrip('.csv')+'_total_frequency.png', bbox_inches='tight')

    ##### RELATIVE_FREQUENCY #####
    fig, ax = pyplot.subplots(figsize=(12, 4))
    # ax2 = ax.twinx()
    for key, grp in df.groupby(['Company']):
        l1, = ax.plot(grp['Year'], grp['Cosine-similarity_Relative_Frequency'], label=key)
        # l2, = ax2.plot(grp['Year'], grp['Overlap-coefficient'], linestyle='dashed')
    ax.legend()
    pyplot.legend(loc='upper right')
    pyplot.title("Plot comparing keyword frequencies between \n the companies and UN")
    pyplot.xlabel("Publishing year of agreement document of the companies")
    pyplot.ylabel("Document's cosine-similarity of relative frequencies")
    # ax2.set_ylabel('Overlap-coefficient', color='b')
    pyplot.show()
    fig.savefig('new-plots/'+file.lstrip('new-data/').rstrip('.csv') + '_relative_frequency.png', bbox_inches='tight')


if __name__ == '__main__':
    # file = 'Paris_full_2_calc_results_for_relative_frequency.csv'
    # prepare_data_from_excel_to_plot(file)
    # file = 'Glasgow_2_calc_results_for_relative_frequency.csv'
    # prepare_data_from_excel_to_plot(file)
    # file = 'Katowice_2_calc_results_for_relative_frequency.csv'
    # prepare_data_from_excel_to_plot(file)
    # #------------Plot 2-grams-----------
    # # file = 'Paris_full_2_calc_results_for_relative_frequency.csv'
    # # prepare_data_from_excel_to_plot(file)
    path = "new-data/*.csv"
    for name in glob.glob(path):
        print(name)
        prepare_data_from_csv_to_plot(name)