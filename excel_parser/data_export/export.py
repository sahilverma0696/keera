'''
Module to read a standard excel file and export 
the data to json file, of same excel_file name.

The first column of excel file is considred as index
'''


import pandas as pd
from sys import argv,exit

def read(file_name):
    df = pd.read_excel(file_name,index_col =0)
    return df


def export_json(df,file_name):
    df.to_json(str(file_name)+".json" ,orient = 'records')


def export(excel_file):
    try:
        df= read(excel_file)
        file_name = str(excel_file).split(".")[0]
        export_json(df,file_name)
    except:
        print("Excel Data not correct.")
        exit(0)

#export(argv[1])

