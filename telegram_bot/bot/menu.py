

import bot_file 
import utils
import os
from pprint import pprint 
import bot_loc
from datetime import datetime

    
TOKEN = utils.read_token("credentials.ini") 



def text_handler(bot,msg,chat_id): 
    # method to handle the text inputs in bot
    text = msg['text'];from_name = msg['from']['first_name']
    #print(chat_id,from_name,text)
    if(text.lower() in "helloheygoodmorningyohi"):
        bot.sendMessage(chat_id,"Hello,it's Spacemonk.Here's all I can do for you")
        bot.sendMessage(chat_id,"Generate Workorder(JSON)\nConvert to standard format.\nImage sending.\nFinding Site(location) \nFinding peers")
    
    
    elif(text.lower() in '1make workorder'):
        bot.sendMessage(chat_id,"Sure, let's get started")
        bot_file.yml_questions(bot,msg,chat_id)


    elif(text.lower() in "2generate json"):
        bot_file.bot.sendMessage(chat_id,"Sure, please upload the std excel format")
        bot_file.file_download(bot,msg,chat_id)


    elif(text.lower()[0:5] in "locate"):
        location = bot_loc.locate(msg)
        if(location is False):
            bot.sendMessage(chat_id,"Location not found")
        else:
            bot.sendLocation(chat_id,location[0],location[1])
    elif(text.lower()[0:3] in "peer"):
        name = msg["text"][5:]
        location =bot_loc.send_location(name)
        if(location == False):
            bot.sendMessage(chat_id,"User Not found")
        else:
            date,latitude,longitude = location
            bot.sendLocation(chat_id,latitude,longitude)
            date= str(datetime.fromtimestamp(date))
            time = date[12:]
            date =date[0:10]
            bot.sendMessage(chat_id,"Last Update at Date: "+date+" Time :"+time)


    else:
        bot.sendMessage(chat_id,"Sorry I don't understand that.")



def menu(bot,msg,content_type,chat_id):
    # menu for the bot,redirects the navigation based on the type of data
    
    if(content_type=='text'):
        # text type input 
        text_handler(bot,msg,chat_id)


    elif(content_type== 'document'):
        # document type input 
        bot_file.file_download(bot,msg,chat_id,TOKEN)


    elif(content_type=='photo'):
        # photo type input 
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
        # location types input
        latitude,longitude =msg["location"]['latitude'],msg["location"]['longitude']
        #bot.sendLocation(chat_id,latitude,longitude)
        bot_loc.save_location(msg,chat_id)
        #bot.sendMessage(chat_id,"Location Updated")
    else:
        # other type input 
        bot.sendMessage(chat_id,"Sorry I don't understand the Data")
        


