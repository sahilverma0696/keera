from io_handles import *
from df_functions import *
from export import export_json

if(check_arguments()==False):
    sys.exit(0)

if(check_all):
    excel_file = pd.ExcelFile(excel_file())
    yml_data = yml_file()
    print(yml_data)
else:
    print("False")
    sys.exit(0)


number_of_sheets = len(excel_file.sheet_names)



def base_df(excel_file,i):
    df = pd.read_excel(excel_file,sheet_name=excel_file.sheet_names[i],header = None)

    
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


def execute(i):
    df = base_df(excel_file,i)
    

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
    df_act.to_excel(excel_file.sheet_names[i]+".xlsx")
    export_json(df_act,excel_file.sheet_names[i])
    print(excel_file.sheet_names[i], " succesfull")




for i in range(number_of_sheets):
    execute(i)