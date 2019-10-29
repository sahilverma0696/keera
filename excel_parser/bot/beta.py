#TODO: Make the bot export_json function by having the file


import telepot 
from telepot.loop import MessageLoop
from time import sleep
from pprint import pprint
#from telegram import File
TOKEN = "970138714:AAE2zD2XT252iZ1ggiWiTMg9nzPh09TJmuM"
bot = telepot.Bot(TOKEN)

def yml_questions(chat_id):
    bot.sendMessage(chat_id,"Please answer the following questions.")
#def gen_json():

def text_handler(msg,chat_id): 
    text = msg['text'];from_name = msg['from']['first_name']
    print(chat_id,from_name,text)
    if(text == 'Make workorder'):
        bot.sendMessage(chat_id,"Sure, let's get started")
        yml_questions(chat_id)
    elif(text =="generate json"):
        bot.sendMessage(chat_id,"Sure, please upload the std excel format")
    else:
        bot.sendMessage(chat_id,"Sorry I don't understand that.")
    
def file_handle(msg):
    file_id = msg['document']['file_id']
    print(bot.getFile(file_id))
    '''download_file =File
    download_file.file_id(file_id)
    download_file.download(custom_path ='./')'''



def handle(msg):
    pprint(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    if(content_type=='text'):
        text_handler(msg,chat_id)
    elif(content_type== 'document'):
        file_handle(msg)

    


MessageLoop(bot,handle).run_as_thread()

print("Running")

while(1):
    sleep(10)