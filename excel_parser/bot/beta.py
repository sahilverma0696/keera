import telepot 
from telepot.loop import MessageLoop
from time import sleep
import os
import random
TOKEN = "970138714:AAE2zD2XT252iZ1ggiWiTMg9nzPh09TJmuM"
bot = telepot.Bot(TOKEN)



def photo_list():
    photo_list =[]
    for each in os.listdir('./photos'):
        photo_list.append(open("./photos/"+each,"rb"))
    return photo_list



x=photo_list()    
    
def handle(msg):
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type,chat_id,chat_type)
    if content_type == "text":
        bot.sendPhoto(chat_id,random.choice(x))
MessageLoop(bot,handle).run_as_thread()

print("Running")

while(1):
    sleep(10)