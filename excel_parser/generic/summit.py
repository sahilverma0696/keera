#!/usr/bin/env python
# coding: utf-8

# To-Do:
#     1. Make the flow proper of functions
#     2. Give completion status of function and complete script
#     3. Make the sheets saved in one file only,(optional, only useful in excel sample export)
# 4. Question: By the time of export, make api calls and excel output or just json.
#     5. Make the file accroding to yaml
# 6. Make proper function, reduce only to logical level.
# 7. Add Pipeline
# ** Handle the exceptions and crashes **

# Flow of functions:
#     1. Drop the nan values, how = all,                        df_dropna(df)
#     2. Convert the df strings to lower case,                  df_to_lower(df)
#     3. Header slicer,                                         upper_mtx_slice(df,header)
#     4. Reset Index of df
#     5. Find coordinates of frequency, make df_freq,           coordinates(df,term)
#     6. Make the activity df by the frequqncy coordinates.
#     7. Set columns for df_act, df_freq,                       set_column(df)
#     8. Extract the week numbers from the df_freq,             week_list(df)
#     9. Merge with the df_act
#     10.Make the modification needed, no week number for dialy and weekly.
#     11.Export the data to required format.

# Crash Handle flow:
#         1.  Checking for the all input files present, else stop
#     2.  Checking the status of a succesfull function or failure
#     3.  Missing value in YAML data
#     4.  Handle the position not found in Matrix
#     5. Mimic the input by sample excel files and yaml data.

# In[ ]:


import pandas as pd
import numpy as np
import yaml
import os
from sys import exit





# ##### IO hadling 

# In[ ]:


with open('../excel_files/Spacemonk/input/data.yml') as file:
    yml_data = yaml.load(file, Loader=yaml.FullLoader)
file.close()


# In[ ]:


os.chdir(yml_data['data_directory'])


# In[ ]:


each_file =0
for files in os.walk(yml_data['data_directory']):
    for each_file in files[2]:
        if ".xlsx" in each_file:
            print("Data File found:\t",each_file)
        
    if(each_file!=0):
        data=each_file
    else:
        print("Data not found")
        exit(1)
## making output directory
if not os.path.exists(yml_data["workorder_directory"]):
    os.makedirs(yml_data["workorder_directory"])
# ##### Data Manipulation 

# In[ ]:


# drop and lowercase, basic on complete df
def df_clean(df):
    # drops the complete null rows and columns in a df
    df.dropna(axis=0,how="all",inplace=True)
    df.dropna(axis=1,how="all",inplace=True)
    # Mapfunction to convert all the string in df to lowercase and keeping the other types same
    return df.applymap(lambda s:s.lower() if type(s) == str else s)


# In[ ]:


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


# In[ ]:


# setting the index of df back from 0
def reset_index(df):
    df.reset_index(inplace=True)
    df.drop(df.columns[0], axis=1,inplace=True)


# In[ ]:


#setting the header, by the first row
def set_column(df):
    df.columns = df.iloc[0]
    df.drop(df.index[0],inplace=True)


# In[ ]:


def week_list(df):
  # finds the count of non nan, in given df, across the rows
  for i in range(1,df.shape[1]+1):
        df.loc[df[i]==df[i],i]=i
  week_num = [[ j for j in i if j ==j] for i in np.array(df) ]
  return week_num


# Data Reading from the files

# In[ ]:


file = pd.ExcelFile(data)


# In[ ]:


number_of_sheets=len(file.sheet_names)



# In[ ]:


def execute(i):
    df = pd.read_excel(file,sheet_name=file.sheet_names[i],header = None)

    
    #Producing clean dataframe in lowercase.

    df =df_clean(df)

    #Creating the dataframe from origin

    origin = coordinates(df,yml_data['origin'])
    assert origin,"Origin not Found"

    df= df.iloc[origin[0]:,origin[1]:]
    reset_index(df)

    #Creating df of frequency

    freq_c =coordinates(df,yml_data['coordinate term'])
    assert freq_c,"Frequency not Found "

    df_freq = df.iloc[freq_c[0]:,freq_c[1]+1:]
    set_column(df_freq)

    df_act = df.iloc[0:,0:freq_c[1]+1]
    set_column(df_act)
    df_act["week number"] = week_list(df_freq)

    df_act.loc[df_act.frequency!=df_act.frequency ,'week number'] = "---"
    df_act.loc[df_act.frequency=='daily' ,'week number'] = "d"
    df_act.loc[df_act.frequency=='weekly' ,'week number'] = "w"

    ##### EXPORTING DATA

    df_act.to_excel(yml_data["workorder_directory"]+"\\"+file.sheet_names[i]+".xlsx")
    print(file.sheet_names[i], " succesfull")



# In[ ]:


for i in range(number_of_sheets):
    execute(i)


# In[ ]:




