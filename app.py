from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    meeting_notes = data.get('notes', '')
    
    if not meeting_notes:
        return jsonify({'error': 'No meeting notes provided'}), 400
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert meeting analyzer. Always respond with valid JSON only, no extra text."
            },
            {
                "role": "user",
                "content": f"""Analyze these meeting notes and extract:
1. Action items with person responsible
2. Decisions made
3. Unresolved issues
4. A follow up email draft for each person

Meeting Notes:
{meeting_notes}

Respond in this exact JSON format:
{{
    "action_items": [{{"person": "name", "task": "task description", "deadline": "deadline if mentioned or empty string"}}],
    "decisions": ["decision 1", "decision 2"],
    "unresolved": ["issue 1", "issue 2"],
    "emails": [{{"person": "name", "email_draft": "email content"}}]
}}"""
            }
        ],
        temperature=0.3,
        max_tokens=1000
    )
    
    result = json.loads(response.choices[0].message.content)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)