import os
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

# Load environment variables from the .env file
load_dotenv()

# Initialize the ElevenLabs client with the API key
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

def text_to_speech(text: str) -> str:
    """Converts text into spoken audio using the ElevenLabs API and plays it.

    Sends the provided text to the ElevenLabs TTS engine using a specific 
    voice ID and settings configured for K.A.M.P.A, then automatically plays 
    the resulting audio stream.

    Args:
        text (str): The text string to be synthesized into speech.

    Returns:
        str: Returns a Spanish error message string if the API call or 
            playback fails. Returns None implicitly upon successful execution.
    """

    try:
        # Calling the text_to_speech conversion API with detailed parameters
        response = elevenlabs.text_to_speech.convert(

            voice_id="KqSsYz0buWgkvSbaGn1n",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_flash_v2_5",
            
            # Optional voice settings that allow you to customize the output
            voice_settings=VoiceSettings(
                stability=1.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
                speed=1.0,
            ),
        )

        # Log success to the console and play the generated audio byte stream
        print("[text_to_speech] Succesfully")
        play(response)

    except Exception as e:
        # Catch and log any exceptions related to the API request or audio playback
        print("[text_to_speech] An error occured while executing text_to_speech. Details:", e)
        return "Ocurrio un error al sintetizar la voz del modelo."



