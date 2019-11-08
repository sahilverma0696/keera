def test_save_location():
    chat_id = 795799315
    with open("xx.txt","r") as f:
        msg = eval(f.read())
    
    save_location(msg,chat_id)
    
#test_save_location()

