from geopy.geocoders import Nominatim
#from textblob import TextBlob
import pandas as pd

# methods to location a place
# Currently workig with string slicing 
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


# method to save the location of peer
location_data = pd.read_csv("./data/location.csv",index_col =False)
def save_location(msg,chat_id):
    global location_data
    entry ={"id":msg["chat"]["id"],
            "first_name":msg["chat"]["first_name"],
            "chat_id":chat_id,
            "date":msg["date"],
            "latitude":msg["location"]["latitude"],
            "longitude":msg["location"]["longitude"]}
    
    entry_loc =location_data[location_data["id"]==msg["chat"]["id"]].index

    if(len(entry_loc) ==0 ):
        location_data =location_data.append(entry,ignore_index =True)
        location_data.to_csv("./data/location.csv",index=False)
        print("Value Saved")
    else:
        entry_loc =location_data[location_data["id"]==msg["chat"]["id"]].index[0]
        location_data.at[entry_loc,"latitude"]=msg["location"]["latitude"]
        location_data.at[entry_loc,"longitude"]=msg["location"]["longitude"]
        location_data.to_csv("./data/location.csv",index=False)
        print("value updated")



    



def send_location(name):
    global location_data
    print(name)
    user =location_data[location_data["first_name"]==name].index
    print(user)
    if(len(user)==0):
        return False
    else:
        user =user[0]
        return (location_data.at[user,"date"],location_data.at[user,"latitude"],location_data.at[user,"longitude"])


