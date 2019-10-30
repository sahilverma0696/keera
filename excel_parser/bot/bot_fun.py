import telegram
import requests
from pprint import pprint 
import sys
sys.path.append('../')
from data_export import export

'''
Folder struct
bot 
    gen_json
            filename_spstd.xlsx
    gen_std
        filename/filename.xlsx
                /dd.yml

'''
import pipe.run as run
import os

def yml_questions(bot,msg,chat_id):
    #bot.sendMessage(chat_id,"Please answer the following questions.")
    #bot.sendMessage(chat_id,"Enter the origin cell")
    bot.sendMessage(chat_id,"Please upload the yml data")

def gen_json(bot,chat_id,file_name):
    export.export("./gen_json/"+file_name)
    bot.sendMessage(chat_id,"Json Generated")


def gen_std(bot,chat_id,file_name):
    os.chdir("./gen_std/")
    # change the yml data name handling,hardcoded right now
    run.run(file_name,"dd.yml")
    print("ExcelStd generate")
    bot.sendMessage(chat_id,"Standard Excel Generated")
    #bot.sendDocument(chat_id,)


def file_download(bot,msg,chat_id,TOKEN):
    # function to download the excel file in the respective folders
    # ./excel_parse
    # ./std_json

    file_id = msg['document']['file_id']
    file_name = msg['document']['file_name']
    pprint(msg) 
    print(file_name) 

    file_name_first =file_name.split(".")[0]
    file_name_ext = file_name.split(".")[1]
    newfile = bot.getFile(file_id)
    url = "https://api.telegram.org/file/bot"+TOKEN+"/"+newfile['file_path']
    r = requests.get(url)
    if(file_name_ext in 'xlsx'):
            
        if( file_name_first[-6:] == "_spstd"):
            open("./gen_json/"+  file_name,'wb').write(r.content)
            gen_json(bot,chat_id,file_name)
            print("Json generated")
        else:
            open("./gen_std/"+file_name,'wb').write(r.content)
            gen_std(bot,chat_id,file_name)
            print("Std excel generated")
    elif(file_name_ext in "yml"):
        open("./gen_std/"+file_name,'wb').write(r.content)
        bot.sendMessage(chat_id,"yml data saved")
            

    
def text_handler(bot,msg,chat_id,TOKEN): 
    text = msg['text'];from_name = msg['from']['first_name']
    print(chat_id,from_name,text)
    if(text.lower() in 'make workorder'):
        bot.sendMessage(chat_id,"Sure, let's get started")
        yml_questions(bot,msg,chat_id)
        
    elif(text.lower() in "generate json"):
        bot.sendMessage(chat_id,"Sure, please upload the std excel format")
        file_download(bot,msg,chat_id,TOKEN)
        

    elif(text.lower() in "helloheygoodmorning"):
        bot.sendMessage(chat_id,"Hello,this is Spacemonk\nwhat can i do for you?\n1. Generate json\n2. Make work order")
    else:
        bot.sendMessage(chat_id,"Sorry I don't understand that.")
    
    

def menu(bot,msg,content_type,chat_id,TOKEN):
    if(content_type=='text'):
        text_handler(bot,msg,chat_id,TOKEN)
    elif(content_type== 'document'):
        file_download(bot,msg,chat_id,TOKEN)
    else:
        bot.sendMessage("Sorry I don't understand that")

