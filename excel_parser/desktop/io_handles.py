# containing all the functionalities realted to the folder and inputs 

import yaml
from os import makedirs, path, listdir,chdir
from sys import exit


try:
    chdir(path.expanduser("~/Desktop/Spacemonk"))
except:
    print("Desktop folder not found please run base_dir")
    exit(0)







def file_check(filetype):
    for files in listdir(path.expanduser("~/Desktop/Spacemonk/input")):
        if filetype in files:
            return files
        else:
            pass
    return False
    


file = file_check(".xlsx")
if(file==False):
    print("\nExcel Data not found\n")
    exit(0)
else:
    excel_data = file
    print("\nExcel Data found:\t",excel_data,'\n')



file = file_check(".yml")
if(file==False):
    print("\nYAML Data not found\n")
    exit(0)
else:
    yml_data = file
    print("\nYAML data found:\t",yml_data,'\n')



    

with open("./input/"+yml_data) as file:
    yml_data = yaml.load(file, Loader=yaml.FullLoader)
file.close()

for keys,values in yml_data.items():
    print(keys,":\t\t\t",values)
