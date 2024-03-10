import requests
import creditals # python file with your creditals
from datetime import datetime
import mic_intergration as mic
import numpy as np

def playingMusic(): # This will print True if music is playing, and False if music is not playing
    url = creditals.ury_url+"/track/nowplaying"
    response = ((((requests.get(url, params={"api_key": creditals.ury_api_key}).text).replace("{","")).replace("}","")).replace('"',"")).split(",") # Gets reponse and puts into an array
    response_array = []
    for entry in response:
        response_array.append(entry.split(":")) # This will split the response into a 2D array (header : value)
    for i in range(0,len(response_array)):
        if response_array[i][0] == "payload":
            if response_array[i][1] == "null":
                return False # No music is playing
            else:
                return False #True # Music is playing

def pressButton(row,column,page):
    url = "http://"+creditals.companion_host+":"+str(creditals.companion_port)+"/api/location/"+str(page)+"/"+str(row)+"/"+str(column)+"/press"
    response = requests.post(url)
    return response.text
    #0,1,creditals.compnaion_page = Go to vis timelord
    #0,2,creditals.compnaion_page = Go to decklink (ATEM)
    #1,1,creditals.compnaion_page = Go to Mic 1 Cam (Pres)
    #1,2,creditals.compnaion_page = Go to Mic 2 & 3 Cam
    #1,3,creditals.compnaion_page = Go to wide Cam

prev_button = [False,False,False]
def pressButtonAvoidRepeat(row,column,page):
    global prev_button
    if prev_button[0] == row and prev_button[1] == column and prev_button[2] == page:
        return "Button already pressed"
    else:
        prev_button = [row,column,page]
        return pressButton(row,column,page)

while True:
    current_time = datetime.now().strftime("%M %S")
    current_min = int(current_time[0:2])
    current_sec = int(current_time[2:5])
    if current_min == 59 or current_min < 2:
        print("News")
        pressButtonAvoidRepeat(0,1,creditals.compnaion_page)
    elif playingMusic() == True:
        print("Music is playing")
        pressButtonAvoidRepeat(0,1,creditals.compnaion_page)
    elif playingMusic() == False:
        print("Music is not playing")
        pressButtonAvoidRepeat(0,2,creditals.compnaion_page)
        mic1_levels, mic2_levels, mic3_levels = [], [], []
        for i in range (0,20):
            mic1_levels.append(mic.is_mic_active(creditals.mic1,creditals.mic1_channel))
            mic2_levels.append(mic.is_mic_active(creditals.mic2,creditals.mic2_channel))
            mic3_levels.append(mic.is_mic_active(creditals.mic3,creditals.mic3_channel))
        mic1_mean = np.mean(mic1_levels)
        mic2_mean = np.mean(mic2_levels)
        mic3_mean = np.mean(mic3_levels)
        if (mic1_mean > creditals.mic_threashold and mic2_mean > creditals.mic_threashold) or (mic2_mean > creditals.mic_threashold and mic3_mean > creditals.mic_threashold) or (mic1_mean > creditals.mic_threashold and mic3_mean > creditals.mic_threashold):
            print("More than one mic is active")
            pressButton(1,3,creditals.compnaion_page)
        elif mic1_mean > creditals.mic_threashold:
            print("Mic 1 is active")
            pressButton(1,1,creditals.compnaion_page)
        elif mic2_mean > creditals.mic_threashold:
            print("Mic 2 is active")
            pressButton(1,2,creditals.compnaion_page)
        elif mic3_mean > creditals.mic_threashold:
            print("Mic 3 is active")
            pressButton(1,2,creditals.compnaion_page)
        else:
            print("No mics are active")
            pressButton(1,3,creditals.compnaion_page)
    else:
        print("Error")
    print("\n------------")
    