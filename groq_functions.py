import os
import json
from groq import Groq
from dotenv import load_dotenv

# Groq ASR function
def speech_to_text(filename, model, ):

    load_dotenv()

    # Initialize the Groq client
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    client = Groq(api_key=GROQ_API_KEY)

    # Specify the path to the audio file
    filename = os.path.dirname(__file__) + "/" + filename # Replace with your audio file!

    # Open the audio file
    with open(filename, "rb") as file:
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
        # To print only the transcription text, you'd use print(transcription.text) (here we're printing the entire transcription object to access timestamps)
        #print(json.dumps(transcription, indent=2, default=str))

    return transcription.text


# Groq LLM function
def get_answer(content, model):

    load_dotenv()

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    client = Groq(api_key=GROQ_API_KEY)

    chat_completion = client.chat.completions.create(
        messages=[
            # Set an optional system message. This sets the behavior of the
            # assistant and can be used to provide specific instructions for
            # how it should behave throughout the conversation.
            {
                "role": "system",
                "content": "You are a helpful assistant called K.A.M.P.A."
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": content,
            }
        ],

        # The language model which will generate the completion.
        model=model
    )

    # Print the completion returned by the LLM.
    return chat_completion.choices[0].message.content


