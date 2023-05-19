import pandas as pd
from matplotlib import pyplot


def prepare_data_from_excel_to_plot(file):
    # This function is used to plot the overlap-score and cos-similarity value for different companies varying with year
    df = pd.read_csv(file, sep=',')
    print(df)
    # df.set_index('Year', inplace=True)
    # df.groupby('Company')['Cos-similarity'].plot(legend=True)
    fig, ax = pyplot.subplots(figsize=(12, 4))
    # ax2 = ax.twinx()
    for key, grp in df.groupby(['Company']):
        l1, = ax.plot(grp['Year'], grp['Cos-similarity'], label=key)
        # l2, = ax2.plot(grp['Year'], grp['Overlap-coefficient'], linestyle='dashed')
    ax.legend()
    pyplot.legend(loc='upper right')
    pyplot.title("Plot comparing keyword frequencies between \n the companies and UN")
    pyplot.xlabel("Publishing year of agreement document of the companies")
    pyplot.ylabel("Document's cosine-similarity")
    # ax2.set_ylabel('Overlap-coefficient', color='b')
    pyplot.show()
    fig.savefig(file+'_without_overlap.png', bbox_inches='tight')


if __name__ == '__main__':
    file = 'T_Paris_full_N_calc_results.csv'
    prepare_data_from_excel_to_plot(file)
    file = 'Glasgow_N_calc_results.csv'
    prepare_data_from_excel_to_plot(file)
    file = 'Katowice_N_calc_results.csv'
    prepare_data_from_excel_to_plot(file)
    #------------Plot 2-grams-----------
    # file = 'Paris_full_2_calc_results_for_relative_frequency.csv'
    # prepare_data_from_excel_to_plot(file)