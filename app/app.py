from flask import Flask, request, render_template
from models.transcribe import transcribe_audio
from models.generate_soap import generate_soap

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("audio_file")
        if not file:
            return "No file uploaded", 400

        file_path = f"temp_{file.filename}"
        file.save(file_path)

        transcript = transcribe_audio(file_path)
        soap_note = generate_soap(transcript)

        return render_template("index.html", transcript=transcript, soap_note=soap_note)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

