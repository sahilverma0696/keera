from time import sleep
def greet(bot,chat_id):
     bot.sendMessage(chat_id,"Hello Welcome to Spacemonk")

def yml_questions(bot,chat_id):
     yml_data = []
     bot.sendMessage(chat_id,"Enter the origin")
     #wait for the input
     yml_data.append(bot.getUpdates()[-1]["message"]["text"])
     bot.sendMessage(chat_id,yml_data)

'''
def latest_offset():
    

def first_message():


def workorder()'''