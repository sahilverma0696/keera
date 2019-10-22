import telepot 
from telepot.loop import MessageLoop
from time import sleep

TOKEN = "970138714:AAE2zD2XT252iZ1ggiWiTMg9nzPh09TJmuM"
bot = telepot.Bot(TOKEN)

response = bot.getUpdates()
offset= response['update_id']
print(offset)
'''
   
def handle(msg):
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type,chat_id,chat_type)
    if content_type == "text":
        bot.sendMessage(chat_id,"Hello")
MessageLoop(bot,handle).run_as_thread()

print("Running")

while(1):
    sleep(10)'''