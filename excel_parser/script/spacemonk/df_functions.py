# all the df related manipulations 

import pandas as pd
from numpy import array
from io_handles import yml_data
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
  for i in range(1,df.shape[1]+1):
        df.loc[df[i]==df[i],i]=i
  week_num = [[ j for j in i if j ==j] for i in array(df) ]
  return week_num



def base_df(file,i):
    df = pd.read_excel(file,sheet_name=file.sheet_names[i],header = None)

    
    #Producing clean dataframe in lowercase.

    df =df_clean(df)
    df =df.applymap(lambda s:s.lower() if type(s) == str else s)

    #Creating the dataframe from origin
    try:
        origin = coordinates(df,yml_data['origin'])
    except:
        print("Origin not found")
        exit(0)

    df= df.iloc[origin[0]:,origin[1]:]
    reset_index(df)

    return df

def single(df):
    df_act = df.iloc[0:,0:]
    set_column(df_act)
    return df_act

