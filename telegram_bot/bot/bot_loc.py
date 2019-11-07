from geopy.geocoders import Nominatim
#from textblob import TextBlob


def locate(msg):
    text = msg["text"][6:]
    #blob = TextBlob(text)
    #noun = blob.noun_phrases[0]
    return geocode(text)



def geocode(address):
    geolocator = Nominatim(user_agent ="sahil",timeout =5)
    #print(address)
    location= geolocator.geocode(address)
    if(location is not None):
        return (location.latitude, location.longitude)
    else:
        return False


def save_location(msg,chat_id):

    
