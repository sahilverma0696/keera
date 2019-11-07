from geopy.geocoders import Nominatim
#from textblob import TextBlob
import csv


import sqllite3
def locate(msg):
    text = msg["text"][6:]
    return geocode(text)



def geocode(address):
    geolocator = Nominatim(user_agent ="sahil",timeout =5)
    location= geolocator.geocode(address)
    if(location is not None):
        return (location.latitude, location.longitude)
    else:
        return False


def new_entry(entry):

    with open("./data/location.csv", "a") as location_data:
        writer = csv.writer(location_data,lineterminator='\n',delimiter=",")
        writer.writerow(entry)




def save_location(msg,chat_id):
    entry =[msg["chat"]["username"],
            msg["chat"]["first_name"],
            chat_id,
            msg["date"],
            msg["location"]["latitude"],
            msg["location"]["longitude"]]
    new_entry(entry)
    
def test_save_location():
    chat_id = 795799315
    with open("xx.txt","r") as f:
        msg = eval(f.read())
    save_location(msg,chat_id)
    
    

    
