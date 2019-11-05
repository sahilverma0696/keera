from configparser import ConfigParser
import requests
def read_token(file_name):
    config = ConfigParser()
    config.read(file_name)
    config = {s:dict(config.items(s)) for s in config.sections()}
    return config["bot_token"]["token"]

#print(read_token("credentials.ini"))


def bot_download(bot,file_id,token):
    newfile = bot.getFile(file_id)
    url = "https://api.telegram.org/file/bot"+token+"/"+newfile['file_path']
    r = requests.get(url)
    return r.content

def bot_download_image(bot,msg,token,content_type):
    if(content_type=="photo"):
        image_id = msg["photo"][0]["file_id"]
        raw_image = bot_download(bot,image_id,token)
        open("./"+  image_id+".jpeg",'wb').write(raw_image)
        return 0
    else:
        return 1
def bot_send_image(bot,chat_id,image):
    image_file = open(image,"rb")
    bot.sendPhoto(chat_id,image_file)
    image_file.close()
    return 0
