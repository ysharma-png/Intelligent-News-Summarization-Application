# 📰 Intelligent News Summarizer Application

An AI-powered web application that summarizes lengthy news articles into concise and meaningful summaries using Azure Cognitive Services and Flask. The application also supports text translation to improve accessibility and user experience.

## 🔗 Project Links

🌐 Live Website: https://your-app-name.onrender.com

📂 GitHub Repository: https://github.com/ysharma-png/Intelligent-News-Summarization-Application.git
---

## 🚀 Features

- 🔹 Automatic news article summarization
- 🔹 Multi-language translation support
- 🔹 Clean and responsive user interface
- 🔹 Fast text processing using Azure AI Services
- 🔹 Flask-based backend integration
- 🔹 Secure API key handling using `.env`
- 🔹 Easy-to-use and lightweight application

---

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Cloud & AI Services
- Azure Text Analytics
- Azure Translator API

### Other Tools
- Git & GitHub

---

## 🌍 Deploy This Website (Public Link)

Since this is a Flask backend app, deploy it on Render (not GitHub Pages).

1. Push your latest code to GitHub.
2. Go to Render dashboard and create a new **Web Service**.
3. Connect this GitHub repository.
4. Set:
   - **Runtime:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Add environment variable:
   - `OPENAI_API_KEY=your_key_here`
6. Deploy and copy the generated Render URL.
7. Replace `https://your-app-name.onrender.com` above with your actual live link.

---

## 📂 Project Structure

```bash
NEWS_SUMMARIZER/
│
├── static/
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── summarizer.py
├── translator.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
