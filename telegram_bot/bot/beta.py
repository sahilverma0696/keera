#!/usr/bin/env python
#TODO: Add log for the bot 

import telepot 
from telepot.loop import MessageLoop
from time import sleep
import utils
import menu
from pprint import pprint 



TOKEN = utils.read_token("credentials.ini")
bot = telepot.Bot(TOKEN)



def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    #print(content_type)
    #pprint(msg)
    #print(chat_id)
    #key,value = msg.items()
    #print(msg_key[3])
    menu.menu(bot,msg,content_type,chat_id)
    
    


MessageLoop(bot,handle).run_as_thread()


print("Bot Running")
while(1):
    sleep(10)