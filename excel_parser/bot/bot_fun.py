import telegram

def yml_questions(bot,chat_id):
    bot.sendMessage(chat_id,"Please answer the following questions.")
#def gen_json():

def text_handler(bot,msg,chat_id): 
    text = msg['text'];from_name = msg['from']['first_name']
    print(chat_id,from_name,text)
    if(text == 'Make workorder'):
        bot.sendMessage(chat_id,"Sure, let's get started")
        yml_questions(bot,chat_id)
    elif(text =="generate json"):
        bot.sendMessage(chat_id,"Sure, please upload the std excel format")
    else:
        bot.sendMessage(chat_id,"Sorry I don't understand that.")
    
def file_handle(bot,msg):
    file_id = msg['document']['file_id']
    file_id = bot.getFile(file_id)
    print(file_id)
    newfile = bot.getFile(file_id['file_id'])
    print(newfile)
    #file_path =file_id['file_path']
    #download_file = bot.download_file(file_id['file_id'],dest = "./")
    
    #download = telegram.File(file_id=file_id['file_id'],bot=bot,file_size =file_id['file_size'],file_path=file_id['file_path'])
    #download.download()

def menu(bot,msg,content_type,chat_id):
    if(content_type=='text'):
        text_handler(bot,msg,chat_id)
    elif(content_type== 'document'):
        file_handle(bot,msg)

