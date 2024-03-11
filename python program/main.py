import requests
import credentials # python file with your credentials
from datetime import datetime
import mic_intergration as mic
import numpy as np

def playingMusic(): # This will print True if music is playing, and False if music is not playing
    url = credentials.ury_url+"/track/nowplaying"
    response = ((((requests.get(url, params={"api_key": credentials.ury_api_key}).text).replace("{","")).replace("}","")).replace('"',"")).split(",") # Gets reponse and puts into an array
    response_array = []
    for entry in response:
        response_array.append(entry.split(":")) # This will split the response into a 2D array (header : value)
    for i in range(0,len(response_array)):
        if response_array[i][0] == "payload":
            if response_array[i][1] == "null":
                return False # No music is playing
            else:
                return True # Music is playing

def pressButton(row,column,page):
    url = "http://"+credentials.companion_host+":"+str(credentials.companion_port)+"/api/location/"+str(page)+"/"+str(row)+"/"+str(column)+"/press"
    response = requests.post(url)
    return response.text
    #0,1,credentials.compnaion_page = Go to vis timelord
    #0,2,credentials.compnaion_page = Go to decklink (ATEM)
    #1,1,credentials.compnaion_page = Go to Mic 1 Cam (Pres)
    #1,2,credentials.compnaion_page = Go to Mic 2 & 3 Cam
    #1,3,credentials.compnaion_page = Go to wide Cam

prev_button = [False,False,False]
def pressButtonAvoidRepeat(row,column,page):
    global prev_button
    if prev_button[0] == row and prev_button[1] == column and prev_button[2] == page:
        return "Button already pressed"
    else:
        prev_button = [row,column,page]
        return pressButton(row,column,page)

if __name__ == "__main__":
    confirm_pres = False
    confirm_guest = False
    confirm_wide = False
    while True:
        confirm_pres = False
        confirm_guest = False
        confirm_wide = False
        current_min = int(datetime.now().strftime("%M"))
        if current_min < 2:
            print("News")
            pressButtonAvoidRepeat(0,1,credentials.compnaion_page)
        elif playingMusic() == True:
            print("Music is playing")
            pressButtonAvoidRepeat(0,1,credentials.compnaion_page)
        elif playingMusic() == False:
            print("Music is not playing")
            pressButtonAvoidRepeat(0,2,credentials.compnaion_page)
            mic1_levels, mic2_levels, mic3_levels, mic4_levels = [], [], [], []
            for i in range (0,20):
                mic1_levels.append(mic.is_mic_active(credentials.mic1,credentials.mic1_channel))
                mic2_levels.append(mic.is_mic_active(credentials.mic2,credentials.mic2_channel))
                mic3_levels.append(mic.is_mic_active(credentials.mic3,credentials.mic3_channel))
            mic1_mean = np.mean(mic1_levels)
            mic2_mean = np.mean(mic2_levels)
            mic3_mean = np.mean(mic3_levels)
            if mic1_mean > credentials.mic_threashold or mic2_mean > credentials.mic_threashold or mic3_mean > credentials.mic_threashold:
                if mic1_mean > mic2_mean and mic1_mean > mic3_mean:
                    print("Presenter Mic (1) is active")
                    print(confirm_pres)
                    if confirm_pres == True:
                        pressButton(1,1,credentials.compnaion_page)
                        confirm_guest,confirm_wide = False, False
                    else:
                        confirm_pres, confirm_guest, confirm_wide = True, False, False
                elif mic2_mean > mic1_mean or mic3_mean > mic1_mean:
                    print("Guest Mic(s) (2, 3 or 4) are active")
                    print(confirm_guest)
                    if confirm_guest == True:
                        pressButton(1,2,credentials.compnaion_page)
                        confirm_pres,confirm_wide = False, False
                    else:
                        confirm_pres, confirm_guest, confirm_wide = False, True, False
            else:
                print("No mics are active")
                print(confirm_wide)
                if confirm_wide == True:
                    pressButton(1,3,credentials.compnaion_page)
                    confirm_pres,confirm_guest = False, False
                else:
                    confirm_pres, confirm_guest, confirm_wide = False, False, True
        else:
            print("Error")
        print("\n------------")