import os
import uuid
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import time

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

# Create and plays K.A.M.P.A's voice
def text_to_speech_file(text: str) -> str:

    # Calling the text_to_speech conversion API with detailed parameters
    response = elevenlabs.text_to_speech.convert(

        voice_id="KqSsYz0buWgkvSbaGn1n", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_flash_v2_5", # Use the flash model for low latency
        
        # Optional voice settings that allow you to customize the output
        voice_settings=VoiceSettings(
            stability=1.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )

    play(response)


