import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_soap(transcript):
    prompt = f"""
    You're a medical assistant. Given the transcript of a clinical visit below, extract SOAP notes.

    TRANSCRIPT:
    {transcript}

    Respond in JSON with four fields: subjective, objective, assessment, and plan.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a medical assistant that extracts SOAP notes from transcripts."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content

