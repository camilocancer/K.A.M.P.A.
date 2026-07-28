
from capture_audio_function import record
from groq_functions import speech_to_text
from groq_functions import get_answer
from elevenlabs_functions import text_to_speech_file
from pathlib import Path

#Choose the model you want
asr_model = 'whisper-large-v3-turbo'
llm_model = "llama-3.1-8b-instant"
file_name = 'user_audiofile.mp3'
file = Path(file_name)

while True:

    input("Press any key to start recording: ")
    record(file_name)
    print('')

    # Call Whisper to transcribe user's audiofile called "user_audiofile.mp3"
    prompt = speech_to_text('/'+file_name, asr_model)
    print("Prompt:")
    print(prompt)
    print('')

    # Call K.A.M.P.A to get an answer based on the transcribed audiofile
    output = get_answer(prompt, llm_model)
    print("K.A.M.P.A:")
    print(output)
    print('')

    text_to_speech_file(output)
    print('---------------')

    # Deletes the file to don't have to rewrite or create a new one in the next round 
    file.unlink()

    continues = input('Do you want to ask another question? (y/n): ')

    if continues != 'y'.lower():
        break

    print('---------------')
    print('')






















