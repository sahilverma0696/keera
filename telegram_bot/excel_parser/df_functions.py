# all the df related manipulations 

import pandas as pd
from numpy import array
from sys import exit



# drop and lowercase, basic on complete df
def df_clean(df):
    # drops the complete null rows and columns in a df
    df.dropna(axis=0,how="all",inplace=True)
    df.dropna(axis=1,how="all",inplace=True)
    # Mapfunction to convert all the string in df to lowercase and keeping the other types same
    return df




# method to return the (row,column), of first occurance, else False
def coordinates(df,term):
    for i in range(len(df.columns)):
        x=df[df.columns[i]].str.find(term)
        if(len(x.index[x==0])==0):
            pass
        else:
            x=int(x.index[x==0][0])
            return (x,i)  
    return False



# setting the index of df back from 0
def reset_index(df):
    df.reset_index(inplace=True)
    df.drop(df.columns[0], axis=1,inplace=True)



#setting the header, by the first row
def set_column(df):
    df.columns = df.iloc[0]
    df.drop(df.index[0],inplace=True)



def week_list(df):
  # finds the count of non nan, in given df, across the rows
    try:
        for i in range(1,df.shape[1]+1):
            df.loc[df[i]==df[i],i]=i
        week_num = [[ j for j in i if j ==j] for i in array(df) ]
        return week_num
    except:
        print("Excel Data is incorrect.")
        exit(0)
        


def single(df):
    df_act = df.iloc[0:,0:]
    set_column(df_act)
    return df_act

