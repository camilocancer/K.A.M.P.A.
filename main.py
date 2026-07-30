from core.capture_audio import capture_audio
from core.stt import speech_to_text
from core.llm import run_conversation
from core.tts import text_to_speech
from pathlib import Path

#Choose the model you want
asr_model = 'whisper-large-v3-turbo'
llm_model = "openai/gpt-oss-120b"
file_name = 'user_audiofile.mp3'
file = Path(file_name)

# List of known exception messages returned by the LLM wrapper
groq_exeptions = ["Ha fallado la autenticación. Revisá que la API Key esté bien.",
                  "Has superado el límite de peticiones. Espera un momento.",
                  "Detecte una solicitud invalida. Revisa el retorno de las herramientas vinculadas.",
                  "Ha ocurrido un error en los servidores de Groq.",
                  "Ha ocurrido un error interno del sistema."]

# Initialize persistent chat memory with system instructions
chat_memory = [{

        "role":"system",
        "content":"You are a helpuf assistant called 'KAMPA'. Ultra-short answers in plane text, no items."
    }
    ]

while True:
    """Main execution loop for KAMPA, handling audio capture, transcription, 
    conversational turns, error checking, text-to-speech synthesis, and cleanup.
    """

    # Wait for user input to trigger audio recording
    input("Presiona cualquier tecla para comenzar a grabar: ")

    # Capture microphone input into the target audio file
    record_result = capture_audio(file_name)
    if record_result == "Ha ocurrido un error capturando el audio.":
        text_to_speech(record_result)
        break

    # Call Whisper to transcribe user's audiofile called "user_audiofile.mp3"
    prompt = speech_to_text(file_name, asr_model)
    if prompt == "Ocurrio un error al transcribir la voz del usuario.":
        text_to_speech(prompt)
        break

    # Call KAMPA to get an answer based on the transcribed audiofile
    answer, messages = run_conversation(prompt, llm_model, chat_memory)
    if answer in groq_exeptions:
        text_to_speech(answer)
        break

    elif answer == "He excedido el limite de busquedas establecido. Intenta nuevamente.":
        text_to_speech(answer)
        continue

    print("\nKAMPA:", answer)

    # Update persistent chat memory with new messages from the conversation session
    for message in messages:
        if message not in chat_memory:
            chat_memory.append(message)

    # Synthesize and play the model's text response using TTS
    tts_result = text_to_speech(answer)
    if tts_result == "Ocurrio un error al sintetizar la voz del modelo.":
        break

    print('\n---------------')

    # Deletes the file to don't have to rewrite or create a new one in the next round 
    file.unlink()

    # Prompt the user to decide whether to continue chatting or exit the loop
    continues = input('¿Queres continuar chateando con KAMPA? (s/n):')

    if continues.lower() != 's':
        break
      
    print('---------------\n')






















