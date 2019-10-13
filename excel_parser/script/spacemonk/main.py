# main execution script
# major calling functions to be made

from io_handles import *
from df_functions import *
from os import path


file = pd.ExcelFile("./input/"+excel_data)


number_of_sheets=len(file.sheet_names)



def execute(i):
    df = base_df(file,i)
    

    ## TODO: seprate the normal df construct vs period data construct 

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

    df_act.to_excel(path.expanduser("~/Desktop/Spacemonk/output/")+file.sheet_names[i]+".xlsx")
    df_act.to_json(path.expanduser("~/Desktop/Spacemonk/output/")+file.sheet_names[i]+".json" ,orient = 'records')
    print(file.sheet_names[i], " succesfull")




for i in range(number_of_sheets):
    execute(i)