from flask import Flask, request, jsonify
from WhisperSTTModel import pipe
import librosa

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to LinkAI.\nSpeech to Text Part."


@app.route('/stt', methods=['POST'])
def convert_voice_to_text():
    audio_file = request.files['audio']
    audio_data, _ = librosa.load(audio_file, sr=16000)
    text = pipe(audio_data)['text'].strip()
    return jsonify({'text': text})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
