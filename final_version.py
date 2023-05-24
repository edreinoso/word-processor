import pandas as pd
from numpy import dot
from numpy.linalg import norm
import csv
from openpyxl import Workbook

'''
This function is a critical-function which extracts the common-words between the respective 1-grams and 2-grams extracted 
from the documents of companies and the UN for each of the agreements.
'''
def prepare_data_from_excel(file, sheet, start, last_useful_col):
    # We only focus on first three columns - common-keyword, relative-frequency in UN, relative-frequency in Company_Year (others not relevant)
    # sorting of data in csv is important for our program, otherwise the merging will not work
    list_col = []
    df = pd.read_excel(file,sheet_name=sheet)
    u = df.select_dtypes(object)
    df[u.columns] = u.apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))
    df_un = df.iloc[:,[0,1,2]].sort_values([start],ascending=[True])
    df_un = df_un[~df_un[start].isna()]
    df_un = df_un.rename(columns={start: "keyword",})
    # comp = df.iloc[:, [4,6]].sort_values(['BP_11'], ascending=[True])
    # comp = comp[~comp['BP_11'].isna()]
    # comp = comp.rename(columns={'BP_11': "keyword"})
    # df_comp = comp.merge(df_un, on='keyword')
    for i in range(4, last_useful_col+1, 4):  # last_useful_col+1, so that last column is included in the iteration
        list_col.append(df.columns[i])
    print(list_col)
    with open(sheet+'_calc_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['Company', 'Year', 'Overlap-coefficient', 'Cosine-similarity_Total_Frequency', 'Cosine-similarity_Relative_Frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for idx, x in enumerate(list_col):
            print(f"----------------Sheet: {sheet}, ---------------Iteration: {idx}-----------------")
            temp = df.iloc[:,[(4*idx)+4,(4*idx)+5, (4*idx)+6]].sort_values([x], ascending=[True])
            temp = temp[~temp[x].isna()]
            temp = temp.rename(columns={x: "keyword"})
            df_test = temp.merge(df_un, on='keyword') # bible of the merge functionality - extract common keywords for UN and a company
            df_test = df_test.rename(columns={"keyword":"keyword_"+x})
            with pd.ExcelWriter('new-data/data_merged_file.xlsx', mode='a', if_sheet_exists='overlay') as excel_writer:
                df_test.to_excel(excel_writer, sheet_name=sheet, startcol=5*idx, index=False)
            overlap_coefficient = (len(df_test.index) / len(df_un.index)) * 100
            print(f"Overlap coefficient {idx}:-------------{overlap_coefficient}")
            list_a_total = df_test.iloc[:, 1].values.tolist()  # Company's total-frequency values in list of common-words
            list_a_relative = df_test.iloc[:, 2].values.tolist()  # Company's relative-frequency values in list of common-words
            list_b_total = df_test.iloc[:, 3].values.tolist()  # UN's total-frequency values in list of common-words
            list_b_relative = df_test.iloc[:, 4].values.tolist()  # UN's relative-frequency values in list of common-words
            similarity_total = cosine_similarity(list_a_total, list_b_total, x)
            similarity_relative = cosine_similarity(list_a_relative, list_b_relative, x)
            string = x.rsplit('_')
            company = string[0]
            year = string[-1]
            # write to a CSV above company, year and cosine-similarity calculation for each of the company-UN pair of common-keywords
            writer.writerow({'Company': company, 'Year': '20'+year, 'Overlap-coefficient': overlap_coefficient,
                             'Cosine-similarity_Total_Frequency': similarity_total, 'Cosine-similarity_Relative_Frequency': similarity_relative})

'''
This function calculates the cosine similarity between the two lists supplied to it based on the common keywords, 
corresponding to a company 'x' and the UN respectively
'''
def cosine_similarity(list_a, list_b, x):
    cos_sim = dot(list_a, list_b) / (norm(list_a) * norm(list_b))
    print(f"Cos-similarity with respect to the company {x}= {cos_sim}")
    return cos_sim


'''
This function is another critical-function which extracts the common-words amongst the respective 1-grams and 2-grams 
extracted from the entire documents of companies and the UN for each of the sheets supplied as an input parameter.
'''
def common_data_from_excel(file, sheet, start, last_useful_col, new_name):
    list_col = []
    df = pd.read_excel(file,sheet_name=sheet)
    u = df.select_dtypes(object)
    df[u.columns] = u.apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))
    df_un = df.iloc[:,[0,1,2]].sort_values([start],ascending=[True])
    df_un = df_un[~df_un[start].isna()]
    df_un = df_un.rename(columns={start: "keyword"})
    for i in range(0, last_useful_col+1, 4):  # last_useful_col+1, so that last column is included in the iteration
        list_col.append(df.columns[i])
    print(list_col)
    df_test = df_un
    df_again = df_un
    un = set(df_un.keyword)
    # 1st round - Go till end, and find common words
    for idx, x in enumerate(list_col):
        temp = df.iloc[:,[(4*idx)+0,(4*idx)+1, (4*idx)+2]].sort_values([x], ascending=[True])
        temp = temp[~temp[x].isna()]
        temp = temp.rename(columns={x: "keyword"})
        un = set.intersection(set(temp.keyword), un)
    common_last = un
    # print(common_last)
    df_again = pd.DataFrame()
    # 2nd round - Iterate through all values, and find the intersection and concat the dataframe
    for idx, x in enumerate(list_col):
        print(f"----------------Sheet: {sheet}, ---------------Iteration: {idx}-----------------")
        temp = df.iloc[:,[(4*idx)+0,(4*idx)+1, (4*idx)+2]].sort_values([x], ascending=[True])
        temp = temp[~temp[x].isna()]
        df_again = pd.concat([temp[temp[x].isin(common_last)]])   #.sort_values(by=x)
        # write to a CSV the common keywords (and associated frequencies) which were found throughout the sheet amongst all company and UN-pairs
        with pd.ExcelWriter(new_name, mode='a', if_sheet_exists='overlay') as excel_writer:
            df_again.to_excel(excel_writer, sheet_name=sheet, startcol=3 * idx, index=False)


if __name__ == '__main__':
    # create Excel file only once for saving the merged data frames
    # new_name = 'new-data/Overall_common_words.xlsx'
    # wb = Workbook()
    # wb.save(new_name)
    file = 'Thesis_POL_U3.xlsx'
    # sheet = 'T_Paris_full_N'
    # start = 'UN_par'
    # last_useful_col = 240
    # prepare_data_from_excel(file, sheet, start, last_useful_col)
    sheet = 'Glasgow_N'
    start = 'UN_gla'
    last_useful_col = 152
    prepare_data_from_excel(file, sheet, start, last_useful_col)
    sheet = 'Katowice_N'
    start = 'UN_kat'
    last_useful_col = 200
    prepare_data_from_excel(file, sheet, start, last_useful_col)
    # ----------2-Grams
    # file = 'Thesis_POL_U3.xlsx'
    # sheet = 'Paris_full_2'
    # start = 'UN_par'
    # last_useful_col = 240
    # prepare_data_from_excel(file, sheet, start, last_useful_col)
    sheet = 'Glasgow_2'
    start = 'UN_gla'
    last_useful_col = 152
    prepare_data_from_excel(file, sheet, start, last_useful_col)
    sheet = 'Katowice_2'
    start = 'UN_kat'
    last_useful_col = 200
    prepare_data_from_excel(file, sheet, start, last_useful_col)
    ######### UN common word calculator #########
    # sheet = 'All_UN_N'
    # start = 'UN_par'
    # last_useful_col = 4
    # prepare_data_from_excel(file, sheet, start, last_useful_col)
    # sheet = 'All_UN_2'
    # start = 'UN_par'
    # last_useful_col = 4
    # prepare_data_from_excel(file, sheet, start, last_useful_col)
    ################### common-words analysis ###################
    # sheet = 'All_N'
    # start = 'UN_par'
    # last_useful_col = 560
    # common_data_from_excel(file, sheet, start, last_useful_col,new_name)
    # sheet = 'All_UN_N'
    # start = 'UN_par'
    # last_useful_col = 8
    # common_data_from_excel(file, sheet, start, last_useful_col, new_name)
    # sheet = 'All_2'
    # start = 'UN_par'
    # last_useful_col = 552
    # common_data_from_excel(file, sheet, start, last_useful_col, new_name)
    # sheet = 'All_UN_2'
    # start = 'UN_par'
    # last_useful_col = 8
    # common_data_from_excel(file, sheet, start, last_useful_col, new_name)