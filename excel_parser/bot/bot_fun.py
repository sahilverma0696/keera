import telegram
import requests
import export
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
    
def file_download(bot,msg,TOKEN):
    file_id = msg['document']['file_id']
    print(msg)  # get the filename through this 
    # organise the local imports 
    # make the download and read folders
    newfile = bot.getFile(file_id)
    #print(newfile)
    url = "https://api.telegram.org/file/bot"+TOKEN+"/"+newfile['file_path']
    r = requests.get(url)
    open('ss.xlsx','wb').write(r.content)
    #export.export(file)



    # try 1
    #file_path =file_id['file_path']
    #download_file = bot.download_file(file_id['file_id'],dest = "./")
    
    # try 2
    #download = telegram.File(file_id=newfile['file_id'],bot=bot,file_size =newfile['file_size'],file_path=newfile['file_path'])
    #download.download()

def menu(bot,msg,content_type,chat_id,TOKEN):
    if(content_type=='text'):
        text_handler(bot,msg,chat_id)
    elif(content_type== 'document'):
        file_download(bot,msg,TOKEN)

