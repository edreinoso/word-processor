import pandas as pd
from scipy.stats import chi2_contingency
from numpy import dot
from numpy.linalg import norm
import csv


def prepare_data_from_excel(file):
    # We only focus on first three columns - common-keyword, relative-frequency in UN, relative-frequency in Company_Year (others not relevant)
    # sorting of data in csv is important for our program, otherwise the merging will not work
    list_col = []
    df = pd.read_excel(file,sheet_name='T_Paris_full_N')
    u = df.select_dtypes(object)
    df[u.columns] = u.apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))
    df_un = df.iloc[:,[0,2]].sort_values(['UN_par'],ascending=[True])
    df_un = df_un[~df_un['UN_par'].isna()]
    df_un = df_un.rename(columns={"UN_par": "keyword",})

    for i in range(4, 240, 4):
        list_col.append(df.columns[i])
    print(list_col)
    with open('T_Paris_full_N.csv', 'w', newline='') as csvfile:
        fieldnames = ['Company', 'Year', 'Overlap-coefficient', 'Cos-similarity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for idx, x in enumerate(list_col):
            print(f"-------------------------------------Iteration: {idx}-------------------------------")
            temp = df.iloc[:,[(4*idx)+4,(4*idx)+6]].sort_values([x], ascending=[True])
            temp = temp[~temp[x].isna()]
            temp = temp.rename(columns={x: "keyword"})
            df_test = temp.merge(df_un, on='keyword')
            overlap_coefficient = (len(df_test.index) / len(df_un.index)) * 100
            print(f"Overlap coefficient {idx}:-------------{overlap_coefficient}")
            list_a = df_test.iloc[:, 1].values.tolist()
            list_b = df_test.iloc[:, 2].values.tolist()
            similarity = cosine_similarity(list_a, list_b, x)
            string = x.rsplit('_')
            company = string[0]
            year = string[-1]
            writer.writerow({'Company': company, 'Year': "20"+year, 'Overlap-coefficient': overlap_coefficient, 'Cos-similarity': similarity})
    # print(f"Overlap coefficient 0:-------------{(len(df_test.index)/len(df_un.index))*100}")
    # print(f"Overlap coefficient 1:-------------{(len(df_test_1.index)/len(df_un.index))*100}")
    # list_a = df_test.iloc[:, 1].values.tolist()
    # list_b = df_test.iloc[:, 2].values.tolist()
    # list_a1 = df_test_1.iloc[:, 1].values.tolist()
    # list_b1 = df_test_1.iloc[:, 2].values.tolist()
    # ax1 = pyplot.subplot()
    # l1, = ax1.plot(list_a, color='red')
    # l2, = ax1.plot(list_b, color='green')
    # # pyplot.scatter(df_test.iloc[:,1], df_test.iloc[:,2])
    # pyplot.legend([l1, l2], ["BP", "UN"])
    # pyplot.show()
    # # chi_squared_cramer_v_influence_analysis(shell_2012, un)
    # print("Cosine test results below:-------------")
    # cosine_similarity(list_a, list_b)
    # cosine_similarity(list_a1, list_b1)


def cosine_similarity(list_a, list_b, x):
    cos_sim = dot(list_a, list_b) / (norm(list_a) * norm(list_b))
    print(f"Cos-similarity with respect to the company {x}= {cos_sim}")
    return cos_sim


if __name__ == '__main__':
    file = 'Thesis_POL (revised).xlsx'
    prepare_data_from_excel(file)