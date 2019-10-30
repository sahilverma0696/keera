import telegram
import requests
from pprint import pprint 
#from data_export import export
import export
#from '../data_export/export' import export

def yml_questions(bot,chat_id):
    bot.sendMessage(chat_id,"Please answer the following questions.")


def gen_json(file_name):
    export.export("./gen_json/"+file_name)


def gen_std(file_name):
    print("ExcelStd generate")


def text_handler(bot,msg,chat_id,TOKEN): 
    text = msg['text'];from_name = msg['from']['first_name']
    print(chat_id,from_name,text)
    if(text.lower() in 'make workorder'):
        bot.sendMessage(chat_id,"Sure, let's get started")
        yml_questions(bot,chat_id)
        
    elif(text.lower() in "generate json"):
        bot.sendMessage(chat_id,"Sure, please upload the std excel format")
        file_download(bot,msg,TOKEN)

    elif(text.lower() in "helloheygoodmorning"):
        bot.sendMessage(chat_id,"Hello, what can i do for you?\ngenerate json\nmakework order")
    else:
        bot.sendMessage(chat_id,"Sorry I don't understand that.")
    
def file_download(bot,msg,TOKEN):
    # function to download the excel file in the respective folders
    # ./excel_parse
    # ./std_json

    file_id = msg['document']['file_id']
    file_name = msg['document']['file_name']
    pprint(msg) 
    print(file_name) 

    file_name_first =file_name.split(".")[0]
    newfile = bot.getFile(file_id)
    url = "https://api.telegram.org/file/bot"+TOKEN+"/"+newfile['file_path']
    r = requests.get(url)

    if( file_name_first[-6:] == "_spstd"):
        open("./gen_json/"+file_name,'wb').write(r.content)
        gen_json(file_name)
        print("Json generated")
    else:
        open("./gen_std/"+file_name,'wb').write(r.content)
        gen_std(file_name)
        print("Std excel generated")
    

def menu(bot,msg,content_type,chat_id,TOKEN):
    if(content_type=='text'):
        text_handler(bot,msg,chat_id,TOKEN)
    elif(content_type== 'document'):
        file_download(bot,msg,TOKEN)

