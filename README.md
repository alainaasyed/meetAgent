# 🤝 MeetAgent — AI-Powered Meeting Intelligence

> Built for Microsoft Agents League Hackathon 2026 | Solo Project by Aliana Begum

![MeetAgent](https://img.shields.io/badge/MeetAgent-AI%20Meeting%20Intelligence-6366f1?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask)
![Groq](https://img.shields.io/badge/Groq-LLaMA%203.3-orange?style=for-the-badge)

---

## 🎯 Problem Statement

Every day, millions of meetings happen across organizations. After each meeting:
- ❌ Action items get forgotten
- ❌ Follow-up emails never get sent
- ❌ Deadlines are missed
- ❌ Team members lose track of decisions

**MeetAgent solves all of this — automatically.**

---

## 💡 What is MeetAgent?

MeetAgent is an AI-powered meeting intelligence agent that transforms rough, unstructured meeting notes into:
- ✅ Structured action items with owners and deadlines
- ✅ Key decisions made during the meeting
- ✅ Unresolved issues that need follow-up
- ✅ Personalized emails auto-sent to each team member
- ✅ Visual deadline tracker with urgency indicators
- ✅ Downloadable PDF report

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 AI Analysis | Extracts action items, decisions, and unresolved issues from rough notes |
| 📊 Meeting Summary | Generates a concise 2-sentence meeting summary |
| 📈 Stats Dashboard | Shows count of actions, decisions, issues at a glance |
| 📅 Deadline Tracker | Visual timeline with color-coded urgency indicators |
| 📧 Auto Email Generation | Creates personalized emails for each team member |
| 📨 One-Click Send | Sends emails directly to recipients via Gmail SMTP |
| 📄 PDF Export | Downloads a professional meeting report |

---

## 🏗️ Architecture
Meeting Notes (Input)
↓
Flask Web Server
↓
Groq API (LLaMA 3.3 70B)
↓
AI Agent Analysis
↓
┌───────────────────────────────┐
│  Action Items  │  Decisions   │
│  Unresolved    │  Summary     │
│  Deadline Tracker             │
└───────────────────────────────┘
↓
Gmail SMTP → Auto Email to each person
↓
PDF Report Generation (ReportLab)

---

## 💡 Microsoft IQ Integration

MeetAgent is designed to integrate with **Microsoft Work IQ** — the intelligence layer behind Microsoft 365 Copilot.

**How Work IQ enhances MeetAgent:**
- Builds memory from past meetings, emails, and chats
- Understands work context and team relationships
- Delivers grounded, cited answers to reduce hallucination
- Connects meeting insights with Microsoft 365 ecosystem

**Current Implementation:**
- Uses Groq API (LLaMA 3.3 70B) for demo purposes
- Architecture is designed for seamless Work IQ integration
- Ready for enterprise deployment with Microsoft 365 Copilot

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Gmail account with App Password
- Groq API key (free at console.groq.com)

### Installation

**1. Clone the repository:**
```bash
git clone https://github.com/alainaasyed/meetAgent.git
cd meetAgent
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables:**
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
GROQ_API_KEY=your_groq_api_key
GMAIL_USER=your_gmail@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password

**4. Run the app:**
```bash
python app.py
```

**5. Open browser:**
http://127.0.0.1:5000

---

## 📁 Project Structure
meetAgent/
├── app.py              # Flask backend + AI agent logic
├── templates/
│   └── index.html      # Frontend UI
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore file
└── README.md           # Project documentation

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + Flask |
| AI Model | Groq API (LLaMA 3.3 70B Versatile) |
| Email | Gmail SMTP |
| PDF | ReportLab |
| Frontend | HTML + CSS + JavaScript |
| Deployment | Local / Azure Ready |

---

## 🎥 Demo

📹 Demo Video: [Watch on YouTube](https://youtu.be/n9VYtQ8vyEw?si=-PLvdq2e9D810BUW)

**Sample Input:**
John will complete the login page by Friday.
Sarah needs to fix the API bug by Wednesday.
We decided to use React for the frontend.
Budget approval is still pending from manager.
Next meeting Tuesday at 10am.

**Sample Output:**
- ✅ 3 action items extracted with owners and deadlines
- 🎯 1 decision identified
- ⚠️ 1 unresolved issue flagged
- 📧 3 personalized emails auto-generated and sent
- 📅 Deadline tracker with color-coded urgency

---

## 👩‍💻 About the Developer

**Aliana Begum** — Final Year B.Tech AI & DS Student
- 🎓 St. Peter's Engineering College, Chennai
- 💼 AI/ML Intern at AutoIntelli
- 🔬 Published researcher — AI in Beauty Industry
- 🔗 [LinkedIn](https://www.linkedin.com/in/aliana-begum)
- 💻 [GitHub](https://github.com/alainaasyed)

---

## 📄 License

MIT License — feel free to use and build upon this project!

---

> Built with ❤️ for Microsoft Agents League Hackathon 2026

