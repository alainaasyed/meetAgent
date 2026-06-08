from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

GMAIL_USER = os.environ.get("GMAIL_USER")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    meeting_notes = data.get('notes', '')
    meeting_title = data.get('title', 'Team Meeting')

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
4. A professional follow up email draft for each person

Meeting Title: {meeting_title}
Meeting Notes:
{meeting_notes}

Respond in this exact JSON format:
{{
    "action_items": [{{"person": "name", "task": "task description", "deadline": "deadline if mentioned or empty string"}}],
    "decisions": ["decision 1", "decision 2"],
    "unresolved": ["issue 1", "issue 2"],
    "emails": [{{"person": "name", "email": "recipient@example.com", "subject": "email subject", "email_draft": "email content"}}],
    "summary": "2 sentence summary of the meeting"
}}"""
            }
        ],
        temperature=0.3,
        max_tokens=1500
    )

    result = json.loads(response.choices[0].message.content)
    return jsonify(result)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    recipient = data.get('email')
    subject = data.get('subject')
    body = data.get('body')

    if not recipient or not subject or not body:
        return jsonify({'error': 'Missing email details'}), 400

    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_USER, recipient, msg.as_string())
        server.quit()

        return jsonify({'success': True, 'message': f'Email sent to {recipient}'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)