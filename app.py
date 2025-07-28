from flask import Flask, request, jsonify
from app.models.generate_soap import generate_soap

app = Flask(__name__)

@app.route('/generate-soap', methods=['POST'])
def generate_soap_endpoint():
    data = request.get_json()
    transcript = data.get('transcript', '')

    if not transcript:
        return jsonify({'error': 'Transcript is required'}), 400

    try:
        soap_notes = generate_soap(transcript)
        return jsonify({'soap_notes': soap_notes})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

