import pandas as pd
from matplotlib import pyplot


def prepare_data_from_excel_to_plot(file):
    # This function is used to plot the overlap-score and cos-similarity value for different companies varying with year
    df = pd.read_csv(file, sep=',')
    print(df)


if __name__ == '__main__':
    file = 'T_Paris_full_N.csv'
    prepare_data_from_excel_to_plot(file)