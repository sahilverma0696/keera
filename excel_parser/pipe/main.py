# main execution script
# major calling functions to be made

from io_handles import *
from df_functions import *
from os import path
import sys


file = pd.ExcelFile(excel_file())


number_of_sheets=len(file.sheet_names)



def execute(i):
    df = base_df(file,i)
    

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

    if not path.exists(path.expanduser("~/Desktop/Spacemonk/output")):
        makedirs(path.expanduser("~/Desktop")+"/Spacemonk/output")
    if(yml_data['excel_copy']):
        df_act.to_excel(path.expanduser("~/Desktop/Spacemonk/output/")+file.sheet_names[i]+".xlsx")
    else:
        pass
    df_act.to_json(path.expanduser("~/Desktop/Spacemonk/output/")+file.sheet_names[i]+".json" ,orient = 'records')
    print(file.sheet_names[i], " succesfull")




for i in range(number_of_sheets):
    execute(i)