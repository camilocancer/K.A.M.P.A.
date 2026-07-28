import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

def record(file_name):

    fs = 44100
    frames = []

    # Runs automatically every time the sound card fills a buffer
    def callback(indata, status, time, status_flags):
        if status_flags:
            print("Warning:", status_flags)

        # Keep a copy of the data received
        frames.append(indata.copy())

    # Open the input stream with no duration limit
    with sd.InputStream(samplerate=fs, channels=1, dtype='float32', callback=callback):
        input("Recording... Press [ENTER] to stop: ")  # Here the program stops and starts waiting for the user to press enter

    print("Processing and saving file...")

    # Concatenate all captured audio blocks into a single array
    complete_file = np.concatenate(frames, axis=0)
        
    # Saves WAV file
    write(file_name, fs, complete_file)




