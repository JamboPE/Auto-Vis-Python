import sounddevice as sd
import numpy as np

def detect_input_audio(data, ):
    global rms
    rms = np.sqrt(np.mean(data**2))
    return rms

def mic_activity_callback(indata, frames, time, status):
    if status:
        print(f"Error in callback: {status}")
        return
    return detect_input_audio(indata)

def is_mic_active(MIC_DEVICE_INDEX):
    # Set the sample rate
    SAMPLE_RATE = 48000 #32000, 44100, 48000, 96000, 128000
    # Start streaming audio input with the callback
    with sd.InputStream(device=MIC_DEVICE_INDEX, callback=mic_activity_callback, channels=1, samplerate=SAMPLE_RATE):
        dummy = "The person who coded this monstrosity"
    return rms