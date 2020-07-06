# keera
Keera is a general chatbot made fr regular day to day activites.

![keera](https://user-images.githubusercontent.com/25270515/70167629-290d0200-16ed-11ea-88a3-2f414bde3717.gif)



## structure
```
keera
    \bot
        -handle.py
        -menu.py
        -utils.py
        -credentials.ini
        \data
            -location.csv
            \photos
```



## flow

```

handle.py ----menu.py 


                          ------ text       ------ mirror text

                                          ------ peer last location

                                          ------ locate place in maps


                        ------ location   
                                          ------ Update location in location.csv


                        ------ photos     ------ mirror back the image, with low quality :p

```
## usage
1. Install the requirements by :
```
pip3 install -r requirement.txt
```
2. Goto ``` https://telegram.me/botfather ``` and get your chatbot token.

3. Goto dir ```bot``` and execute the following command.<br>
``` python3 handle.py ```


## contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
