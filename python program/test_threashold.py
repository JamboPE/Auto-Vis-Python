import mic_intergration as mic
import time
import credentials

print("This will spam you with the current levels of the mic inputs selected in credentials.py,\n press Ctrl+C to exit")
time.sleep(1)
while True:
    print(f"{credentials.mic1}: {mic.is_mic_active(credentials.mic1,credentials.mic1_channel)}")
    print(f"{credentials.mic2}: {mic.is_mic_active(credentials.mic2,credentials.mic2_channel)}")
    print(f"{credentials.mic3}: {mic.is_mic_active(credentials.mic3,credentials.mic3_channel)}")
    print(f"{credentials.mic3}: {mic.is_mic_active(credentials.mic4,credentials.mic4_channel)}")
    print("\n------------")
    time.sleep(1)