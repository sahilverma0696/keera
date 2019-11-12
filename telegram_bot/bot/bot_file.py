# global imports
import requests
from pprint import pprint 
import os
import sys
sys.path.append('../')
from shutil import rmtree


from data_export import export
import excel_parser.parser as parser


def yml_questions(bot,msg,chat_id):
    bot.sendMessage(chat_id,"Please upload the yml data")


def gen_json(bot,msg,chat_id,file_name):
    # method to call export function, generates json file
    os.chdir("./gen_json")
    export.export("./"+file_name)
    os.chdir("..")
    bot.sendMessage(chat_id,"Json Generated")


def std_file_check():
    # method to check for xlsx and yml file in folder
    if(file_check("xlsx")!=False ):
        if(file_check("yml")!= False):
            excel_file = file_check("xlsx")
            yml_file = file_check("yml")
            return (excel_file,yml_file)
    else:
        return False


def file_check(extension):
    # method to check file in a folder
    i = len(extension)
    all_files = os.listdir()
    for each_file in all_files:
        if(each_file[-i:]==extension):
            return each_file
    else:
        return False

# ISSUE: File crash, directory handle if xl file sent first
def gen_std(bot,msg,chat_id,file_name):
    # method to call excel_parser function
    os.chdir("./gen_std/"+msg['from']['username']+"/")
    #print(os.listdir())
    # change the yml data name handling,hardcoded right now
    try:
        if(std_file_check()!=False):
            excel_file,yml_file = std_file_check()
            
            print(excel_file,yml_file)
            parser.parser(excel_file,yml_file)
            print("ExcelStd generate")
            bot.sendMessage(chat_id,"Standard Excel Generated")
            all_files = os.listdir()
            for each_file in all_files:
                if(each_file[-11:]=="_spstd.xlsx"):
                    f =open(each_file,"rb")
                #file_doc = f.read()
                    bot.sendDocument(chat_id,f)
                    f.close()
    except:

        bot.sendMessage(chat_id,"Please upload the yml files again")
    os.chdir("..") 
    rmtree("./"+msg['from']['username'])
    os.chdir("..")



def file_download(bot,msg,chat_id,TOKEN):
    #method to download the incoming document from bot 
    # function to download the excel file in the respective folders
    # ./excel_parse
    # ./std_json

    file_id = msg['document']['file_id']
    file_name = msg['document']['file_name']
    print(msg['from']['username']) 
    print(file_name) 

    file_name_first =file_name.split(".")[0]
    file_name_ext = file_name.split(".")[1]
    newfile = bot.getFile(file_id)
    url = "https://api.telegram.org/file/bot"+TOKEN+"/"+newfile['file_path']
    r = requests.get(url)
    if(file_name_ext in 'xlsx'):
            
        if( file_name_first[-6:] == "_spstd"):
            open("./gen_json/"+  file_name,'wb').write(r.content)
            gen_json(bot,msg,chat_id,file_name)
            print("Json file generated")
        else:
            try:
                os.mkdir("./gen_std/"+msg['from']['username']+"/")
            except:
                pass
            print(os.getcwd())
            open("./gen_std/"+msg['from']['username']+"/"+file_name,'wb').write(r.content)
            gen_std(bot,msg,chat_id,file_name)
            print("Standard Excel generated")
    elif(file_name_ext in "yml"):
        try:
            os.mkdir("./gen_std/"+msg['from']['username']+"/")
        except:
            pass
        #print(os.getcwd())
        open("./gen_std/"+msg['from']['username']+"/"+file_name,'wb').write(r.content)
        bot.sendMessage(chat_id,"YML data saved\n Upload the excel data.")
            

