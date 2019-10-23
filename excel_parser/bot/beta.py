import telepot 
from telepot.loop import MessageLoop
from time import sleep
from pprint import pprint
import bot_fun
TOKEN = "970138714:AAE2zD2XT252iZ1ggiWiTMg9nzPh09TJmuM"
bot = telepot.Bot(TOKEN)

count =1
# to recieve msg regularly
def handle(msg):
    #pprint(msg)
    global count 
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg['text'];from_name = msg['from']['first_name']
    print(chat_id,content_type,from_name,text)
    '''if(count ==1):
        bot_fun.greet(bot,chat_id)
    count = count + 1'''
    #if(text == 'workorders'):
    #    bot_fun.yml_questions(bot,chat_id)

def handle1(msg):
    bot.sendMessage(chat_id,"H")
MessageLoop(bot,handle).run_as_thread()

print("Running")

while(1):
    sleep(10)