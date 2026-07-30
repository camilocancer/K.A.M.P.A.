import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

def capture_audio(file_name):
    """Captures continuous audio from the microphone until user input is received.

    Listens to the default audio input stream, accumulates recorded PCM blocks
    into memory, and exports the final sequence as a WAV file upon completion.

    Args:
        file_name (str): Path or target filename where the recorded WAV file 
            will be saved.

    Returns:
        str or None: Returns an error message string if audio capture fails, 
            otherwise returns None on successful execution.
    """

    # Sample rate in Hz (standard CD quality audio)
    fs = 44100

    # Internal buffer to store incoming raw audio blocks
    frames = []

    # Runs automatically every time the sound card fills a buffer
    def callback(indata, status, time, status_flags):
        """Callback function executed by sounddevice for each incoming audio chunk.

        Args:
            indata (numpy.ndarray): Raw audio data captured in the current frame.
            status (sounddevice.CallbackFlags): Status object representing buffer events.
            time (CData): Timestamps related to input and output buffer timing.
            status_flags (sounddevice.CallbackFlags): Specific buffer warning flags.
        """
     
        if status_flags:
            print("Warning:", status_flags)

        # Keep a copy of the data received
        frames.append(indata.copy())

    try:

        # Open the input stream with no duration limit
        with sd.InputStream(samplerate=fs, channels=1, dtype='float32', callback=callback):
            input("Grabando... Presiona [ENTER] para dejar de grabar\n") # Here the program stops and starts waiting for the user to press enter

        # Concatenate all captured audio blocks into a single array
        complete_file = np.concatenate(frames, axis=0)
            
        # Saves WAV file
        write(file_name, fs, complete_file)
        print("[capture_audio] Succesfully")

    except Exception as e:
        # Log unexpected errors during audio stream processing or file saving
        print("[capture_audio] An error occured while executing capture_audio. Details:", e)
        return "Ha ocurrido un error capturando el audio."





