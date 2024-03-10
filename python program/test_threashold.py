import mic_intergration as mic
import time
import creditals

print("This will spam you with the current levels of the mic inputs selected in creditals.py,\n press Ctrl+C to exit")
time.sleep(1)
while True:
    print(f"{creditals.mic1}: {mic.is_mic_active(creditals.mic1,creditals.mic1_channel)}")
    print(f"{creditals.mic2}: {mic.is_mic_active(creditals.mic2,creditals.mic2_channel)}")
    print(f"{creditals.mic3}: {mic.is_mic_active(creditals.mic3,creditals.mic3_channel)}")
    print("\n------------")
    time.sleep(1)