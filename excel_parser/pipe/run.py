'''
Module to convert the NALPAD excel file to std excel format.
import run() to execute.

run(excel_file.xlsx,yml_data.yml)

'''


import file_handles
from df_functions import *
#from export import export_json
from sys import argv




def base_df(excel_filez,i,yml_data):
    df = pd.read_excel(excel_filez,sheet_name=excel_filez.sheet_names[i],header = None)

    
    #Producing clean dataframe in lowercase.

    df =df_clean(df)
    df =df.applymap(lambda s:s.lower() if type(s) == str else s)
    #Creating the dataframe from origin
    #try:
    origin = coordinates(df,yml_data['origin'])
    #except:
    #    print("Origin not found")
    #    exit(0)

    df= df.iloc[origin[0]:,origin[1]:]
    reset_index(df)

    return df


def execute(i,excel_filez,yml_data):
    df = base_df(excel_filez,i,yml_data)
    

    ## TODO: seprate the normal df construct vs period data construct 
    if(yml_data['periodicity']):
        try:
            freq_c =coordinates(df,yml_data['coordinate term'])
        except:
            print("Frequency not Found ")
            exit(0)
        
        df_freq = df.iloc[freq_c[0]:,freq_c[1]+1:]
        set_column(df_freq)

        df_act = df.iloc[0:,0:freq_c[1]+1]
        set_column(df_act)
        df_act["week number"] = week_list(df_freq)

        df_act.loc[df_act.frequency!=df_act.frequency ,'week number'] = "---"
        df_act.loc[df_act.frequency=='daily' ,'week number'] = "d"
        df_act.loc[df_act.frequency=='weekly' ,'week number'] = "w"

    else:
        df_act = single(df)
        
        


    ##### EXPORTING DATA
    df_act.to_excel(excel_filez.sheet_names[i]+"_spstd.xlsx")
    #export_json(df_act,excel_filez.sheet_names[i])
    print(excel_filez.sheet_names[i], " succesfull")

def run(excel,yml):
    excel_file = pd.ExcelFile(file_handles.excel_file(excel))
    number_of_sheets = len(excel_file.sheet_names)
    yml_data = file_handles.yml_file(yml)
    for i in range(number_of_sheets):
        execute(i,excel_file,yml_data)




#run(argv[1],argv[2])