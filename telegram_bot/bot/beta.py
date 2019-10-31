#TODO: Add log for the bot 

import telepot 
from telepot.loop import MessageLoop
from time import sleep
from pprint import pprint
import bot_fun

# Read token from seprate file
TOKEN = "970138714:AAE2zD2XT252iZ1ggiWiTMg9nzPh09TJmuM"
bot = telepot.Bot(TOKEN)



def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    bot_fun.menu(bot,msg,content_type,chat_id,TOKEN)
    print(content_type)
    


MessageLoop(bot,handle).run_as_thread()


print("Running")

while(1):
    sleep(10)