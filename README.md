# 🤖 Meet My Jarvis

An AI-powered personal desktop assistant built with Python that can automate daily computer tasks, answer questions using a local AI model, and help improve productivity.

---

## ✨ Features

- 🎙️ Voice Command Support
- 🗣️ Text-to-Speech Responses
- 🧠 AI Chat using Ollama (Local LLM)
- 🌐 Google Search
- ▶️ Open YouTube
- 🎵 Play YouTube Songs
- 📧 Open Gmail
- 💻 Open Applications
  - Google Chrome
  - Visual Studio Code
  - Notepad
  - Calculator
  - File Explorer
- ❌ Close Applications
- 📂 Open Files and Folders
- 📁 File Management
- ⚡ Fast Local Execution
- 🔒 Privacy-Friendly (Runs locally with Ollama)

---

## 🛠️ Tech Stack

- Python 3.11+
- Ollama
- Speech Recognition
- pyttsx3
- Webbrowser
- OS
- Subprocess

---

## 📁 Project Structure

```
jarvise/
│
├── app/
│   ├── main.py
│   ├── brain.py
│   ├── commands.py
│   ├── apps.py
│   ├── speak.py
│   ├── listen.py
│   ├── file_manager.py
│   ├── config.py
│   └── test_ollama.py
│
├── .venv/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Gokulsrinivasan-s/meet_my_jarvis.git
```

```bash
cd meet_my_jarvis
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama.

https://ollama.com

Pull the Llama model

```bash
ollama pull llama3
```

Start Ollama

```bash
ollama serve
```

---

# Run Jarvis

From the project root

```bash
python app/main.py
```

or

```bash
cd app
python main.py
```

---

# Example Commands

```
Open Chrome

Open VS Code

Open YouTube

Search Python Tutorial

Play Believer Song

Open Gmail

Open Calculator

Open Downloads Folder

Close Chrome

Close VS Code

What is Artificial Intelligence?

Tell me a joke
```

---

# Future Features

- Face Recognition
- WhatsApp Automation
- Email Automation
- Calendar Integration
- Reminder System
- Weather Updates
- News Updates
- Spotify Control
- Home Automation
- Mobile App
- Windows Startup Assistant
- AI Memory
- Screen Understanding
- OCR
- Image Generation
- File Search
- Chat History
- Multi-language Support
- Smart Task Automation

---

# Requirements

- Python 3.11+
- Ollama
- Windows 10/11
- Microphone
- Internet (for web commands)

---

# Author

**Gokul S**

B.Tech Artificial Intelligence & Data Science

Machine Learning Engineer

GitHub

https://github.com/Gokulsrinivasan-s

LinkedIn

https://www.linkedin.com/in/gokulsrinivasan/

---

# License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful,

⭐ Star the repository

🍴 Fork the project

🐛 Report issues

💡 Suggest new features

---

## 🚀 Vision

The goal of **Meet My Jarvis** is to build an open-source AI assistant that automates everyday computer tasks, integrates with modern AI models, and evolves into a fully featured personal assistant similar to Jarvis from Iron Man while remaining customizable and privacy-friendly.<img width="1360" height="768" alt="Screenshot 2026-07-18 221308" src="https://github.com/user-attachments/assets/7c6d8378-0825-48e2-a9e1-4fc69d85ea18" />
<img width="1360" height="768" alt="Screenshot 2026-07-18 221230" src="https://github.com/user-attachments/assets/9721e7a6-b57d-45f3-8f8d-b73be4cf279f" />
