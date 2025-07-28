import whisper
import os

model = whisper.load_model("base")

def transcribe_audio(file_path):
    try:
        result = model.transcribe(file_path)
        return result["text"]
    except Exception as e:
        return f"Error during transcription: {e}"

