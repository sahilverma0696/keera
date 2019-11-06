

import bot_file 
import utils
import os
from pprint import pprint 
def text_handler(bot,msg,chat_id): 
    # method to handle the text inputs in bot
    text = msg['text'];from_name = msg['from']['first_name']
    #print(chat_id,from_name,text)
    if(text.lower() in "helloheygoodmorningyohi"):
        bot.sendMessage(chat_id,"Hello,it's Spacemonk.Here's all I can do for you")
        bot.sendMessage(chat_id,"1.Generate Workorder(JSON)\n2.Convert to standard format.\n3.Image sending.\n4.Finding Site \n5. Finding peers")
    elif(text.lower() in '1make workorder'):
        bot.sendMessage(chat_id,"Sure, let's get started")
        bot_file.yml_questions(bot,msg,chat_id)
        
    elif(text.lower() in "2generate json"):
        bot_file.bot.sendMessage(chat_id,"Sure, please upload the std excel format")
        bot_file.file_download(bot,msg,chat_id)
    elif(text.lower()[0:5] in "locate"):
        location = utils.locate(msg)
        bot.sendMessage(chat_id,location)

    
    else:
        bot.sendMessage(chat_id,"Sorry I don't understand that.")
    
TOKEN = utils.read_token("credentials.ini") 

def menu(bot,msg,content_type,chat_id):
    # menu for the bot,redirects the navigation based on the type of data
    
    if(content_type=='text'):
        text_handler(bot,msg,chat_id)
    elif(content_type== 'document'):
        
        bot_file.file_download(bot,msg,chat_id,TOKEN)
    elif(content_type=='photo'):
        bot.sendMessage(chat_id,"Image Detected\nDownloading Image")
        os.chdir("./photos")
        image_status =utils.bot_download_image(bot,msg,TOKEN,content_type)

        if(image_status==0):
            bot.sendMessage(chat_id,"Image Downloaded!!")
            image = msg["photo"][0]["file_id"]+".jpeg"
            send_status =utils.bot_send_image(bot,chat_id,image)
            if(send_status==0):
                bot.sendMessage(chat_id,"Image Sent")
            os.chdir("..")
        else:
            bot.sendMessage(chat_id,"Image not Downloaded!!")
    elif(content_type=="location"):
        latitude,longitude =msg["location"]['latitude'],msg["location"]['longitude']
        bot.sendLocation(chat_id,latitude,longitude)
    else:
        bot.sendMessage(chat_id,"Sorry I don't understand that")
        


