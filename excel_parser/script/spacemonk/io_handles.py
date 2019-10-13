# containing all the functionalities realted to the folder and inputs 

import yaml
import os
from sys import exit


try:
    os.chdir(os.path.expanduser("~/Desktop/Spacemonk"))
except:
    print("Desktop folder not found, Please run base_dir")
    exit(0)




def file_check(filetype):
    for files in os.listdir(os.path.expanduser("~/Desktop/Spacemonk/input")):
        if filetype in files:
            return files
        else:
            pass
    return False
    


file = file_check(".xlsx")
if(file==False):
    print("Excel Data not found")
    exit(1)
else:
    excel_data = file
    print("Excel Data found\t",excel_data)



file = file_check(".yml")
if(file==False):
    print("YAML Data not found")
    exit(1)
else:
    yml_data = file
    print("YAML data found\t",yml_data)



    

with open("./input/"+yml_data) as file:
    yml_data = yaml.load(file, Loader=yaml.FullLoader)
file.close()

print(yml_data)

