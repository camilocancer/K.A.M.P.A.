import os
import json
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from the .env file
load_dotenv()

# Initialize the Groq client
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

def speech_to_text(filename, model, ):
    """Transcribes an audio file to text using the Groq Whisper API.

    Resolves the file path relative to the script's parent directory, 
    opens the audio file, and sends it to the Groq API for transcription 
    configured for Spanish language input.

    Args:
        filename (str): The name of the audio file to transcribe, expected 
            to be located in the parent directory of this script.
        model (str): The specific Groq Whisper model identifier to use 
            for the transcription.

    Returns:
        str: The transcribed text string if the API call is successful, 
            or a Spanish error message string if an exception occurs.
    """

    try:
        # Resolve the absolute path to the directory containing this script
        audio_dir = Path(__file__).resolve().parent

        # Construct the full path to the target audio file in the parent directory
        audio_path = audio_dir.parent / filename

        # Open the audio file in binary read mode
        with open(audio_path, "rb") as file:
            # Create a transcription of the audio file
            transcription = client.audio.transcriptions.create(
            file=file, # Required audio file
            model=model, # Required model to use for transcription
            prompt="Specify context or spelling",  # Optional
            response_format="verbose_json",  # Optional
            timestamp_granularities = ["word", "segment"], # Optional (must set response_format to "json" to use and can specify "word", "segment" (default), or both)
            language="es",  # Optional
            temperature=0.0  # Optional
            )

        # Log a success message to the console upon successful API response
        print("[speech_to_text] Succesfully")
        return transcription.text

    except Exception as e:
        # Catch and log any exceptions related to file I/O or the Groq API request
        print("[speech_to_text] An error occured while executing speech_to_text. Details:", e)
        return "Ocurrio un error al transcribir la voz del usuario."

