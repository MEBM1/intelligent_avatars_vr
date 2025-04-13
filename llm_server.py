from flask import Flask, request, jsonify, send_from_directory
import subprocess
import pyttsx3
import os
import whisper
import time
import os
import torchaudio
import traceback

# Flask init
app = Flask(__name__)

# Init Whisper (transcription model)
whisper_model = whisper.load_model("base")  

# start TTS engine
engine = pyttsx3.init()

# settings folder and audio
audio_filename = "response.wav"
audio_directory = os.path.join(os.getcwd(), 'static')
audio_path = os.path.join(audio_directory, audio_filename)

if not os.path.exists(audio_directory):
    os.makedirs(audio_directory)

# Personality Prompt
personality_prompt = """
Você é Marie Curie, uma cientista renomada, conhecida mundialmente por suas contribuições à ciência.
Responda de forma sábia, gentil, didática e breve como se estivesse explicando para um curioso interessado em ciência.
"""

# Endpoint to questions in audio
@app.route('/speech-to-text-and-respond', methods=['POST'])
def speech_to_text_and_respond():
    if 'file' not in request.files:
        return jsonify({"error": "Arquivo de áudio não encontrado."}), 400

    audio_file = request.files['file']
    audio_path = "user_input.wav"
    audio_file.save(audio_path)

    for i in range(10): 
        if os.path.exists(audio_path) and os.path.getsize(audio_path) > 1000:
            break
        time.sleep(0.1)
    else:
        return jsonify({"error": "Arquivo de áudio não salvo corretamente."}), 500

    # Verify if the audio has content (waveform)
    try:
        waveform, sr = torchaudio.load(audio_path)
        if waveform.shape[1] == 0:
            return jsonify({"error": "Áudio vazio ou corrompido."}), 400
    except Exception as e:
        return jsonify({"error": f"Erro ao carregar o áudio: {str(e)}"}), 500

    # Transcription with Whisper
    #print('CAMINHO DO AUDIO', audio_path)
    result = whisper_model.transcribe(audio_path)
    user_text = result['text']
    print("Usuário disse:", user_text)

    # call function ´ask_internal´ with the prompt transcription
    data = {"prompt": user_text}
    response = ask_internal(data)

    # Return transcription and audio generated
    return jsonify({
        "transcription": user_text,
        "response": response["response"],
        "audio_path": response["audio_path"]
    })

# Internal function
def ask_internal(data):
    user_prompt = data.get('prompt')

    # generate full prompt with personality included
    full_prompt = f"{personality_prompt}\nUsuário: {user_prompt}\nAssistente:"
    
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=full_prompt.encode(),
        capture_output=True
    )
    response = result.stdout.decode().strip()

    # Transform answer in audio
    engine.save_to_file(response, audio_path)
    engine.runAndWait()

    return {
        "response": response,
        "audio_path": f"/static/{audio_filename}"
    }


# Endpoint to serve audio
@app.route('/static/<filename>')
def send_audio(filename):
    return send_from_directory(audio_directory, filename)

# Run the server
if __name__ == '__main__':
    app.run(port=5000)