#TODO: Add log for the bot 

import telepot 
from telepot.loop import MessageLoop
from time import sleep
import utils
import bot_fun


# Read token from seprate file
TOKEN = utils.read_token("credentials.ini")
bot = telepot.Bot(TOKEN)



def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    bot_fun.menu(bot,msg,content_type,chat_id,TOKEN)
    
    


MessageLoop(bot,handle).run_as_thread()


print("Bot Running")

while(1):
    sleep(10)