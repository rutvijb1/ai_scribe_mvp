import os
from flask import Blueprint, request, jsonify
import whisper
from app.models.generate_soap import generate_soap

bp = Blueprint('api', __name__)
model = whisper.load_model("base")  # You can use "small" or "medium" if you want higher accuracy

@bp.route('/upload', methods=['POST'])
def upload():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio = request.files['audio']
    audio_path = os.path.join('/tmp', audio.filename)
    audio.save(audio_path)

    try:
        transcript_result = model.transcribe(audio_path)
        transcript_text = transcript_result['text']

        soap_notes = generate_soap(transcript_text)

        return jsonify({
            'transcript': transcript_text,
            'soap_notes': soap_notes
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

