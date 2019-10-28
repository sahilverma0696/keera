from yaml import load,FullLoader

def excel_file(argv1):
    if(str(argv1).split(".")[-1] in "xlsx xls"):
            return argv1
    else:
        print("Excel fail")
        return False


def yml_file(argv2):
    if(str(argv2).split(".")[-1] in "yaml yml"):
        try:
            with open(argv2) as yml_file:
                yml_data = load(yml_file,Loader=FullLoader)
            yml_file.close()
            return yml_data
        except:
            print("YML fail")
            return False
    else:
        print("YML fail")
        return False

