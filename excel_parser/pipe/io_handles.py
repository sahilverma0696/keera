import sys
from yaml import load,FullLoader


def check_arguments():
    if(len(sys.argv)==3):
        return True
    else:
        print("Argument fail")
        return False

def excel_file():
    if(str(sys.argv[1]).split(".")[-1] in "xlsx xls"):
            return sys.argv[1]
    else:
        print("Excel fail")
        return False

def yml_file():
    if(str(sys.argv[2]).split(".")[-1] in "yaml yml"):
        try:
            with open(sys.argv[2]) as yml_file:
                yml_data = load(yml_file,Loader=FullLoader)
            yml_file.close()
            return yml_data
        except:
            print("YML fail")
            return False
    else:
        print("YML fail")
        return False

def check_all():
    if(check_arguments() and excel_file()!= False and yml_file()!= False):
        return True
    else:
        return False

