from configparser import ConfigParser

def read_token(file_name):
    config = ConfigParser()
    config.read(file_name)
    config = {s:dict(config.items(s)) for s in config.sections()}
    return config["bot_token"]["token"]

#print(read_token("credentials.ini"))
