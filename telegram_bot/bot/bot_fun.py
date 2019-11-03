

import bot_file 
import utils
 
def text_handler(bot,msg,chat_id): 
    # method to handle the text inputs in bot
    text = msg['text'];from_name = msg['from']['first_name']
    print(chat_id,from_name,text)
    if(text.lower() in "helloheygoodmorningyohi"):
        bot.sendMessage(chat_id,"Hello,this is Spacemonk bot.\nWhat can I do for you?\n1. Generate json\n2. Make work order \n3. Instructions")
    elif(text.lower() in '1make workorder'):
        bot.sendMessage(chat_id,"Sure, let's get started")
        bot_file.yml_questions(bot,msg,chat_id)
        
    elif(text.lower() in "2generate json"):
        bot_file.bot.sendMessage(chat_id,"Sure, please upload the std excel format")
        bot_file.file_download(bot,msg,chat_id)
        
    
    else:
        bot.sendMessage(chat_id,"Sorry I don't understand that.")
    
    

def menu(bot,msg,content_type,chat_id):
    # menu for the bot,redirects the navigation based on the type of data
    if(content_type=='text'):
        text_handler(bot,msg,chat_id)
    elif(content_type== 'document'):
        TOKEN = utils.read_token("credentials.ini")
        bot_file.file_download(bot,msg,chat_id,TOKEN)
    else:
        bot.sendMessage(chat_id,"Sorry I don't understand that")

