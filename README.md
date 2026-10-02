# CampusFlow

> **One place to manage everything that college throws at you.**

CampusFlow is a student productivity web app that brings assignments, lab records, study resources, class updates, deadlines, and previous papers into one organized place.

## 🚀 Live Demo

**Live App:** https://campusflow-0b7e.onrender.com

## ✨ Features

- 📚 **Assignments**
  - Add assignments
  - Set deadlines
  - Mark assignments as completed
  - Delete assignments

- 🧪 **Lab Records**
  - Add lab experiments
  - Track deadlines
  - Mark records as completed
  - Delete records

- 📝 **Notes & Resources**
  - Save study resources
  - Organize resources by subject
  - Add useful links

- 📢 **Class Updates**
  - Add important class announcements
  - Keep recent updates organized

- ⏰ **Deadlines**
  - View assignment and lab deadlines together
  - Quickly see pending academic work

- 📄 **Previous Papers**
  - Store previous examination papers
  - Organize papers by subject, year, semester, and exam type

- 📊 **Dashboard**
  - View assignment statistics
  - View lab record statistics
  - Track pending work
  - See latest class updates

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Database
- SQLite

### Deployment
- Render

### Version Control
- Git
- GitHub

## 📁 Project Structure

```text
CampusFlow/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    ├── dashboard.html
    ├── assignments.html
    ├── lab-records.html
    ├── resources.html
    ├── class-updates.html
    ├── deadlines.html
    └── previous-papers.html
💻 Run Locally
1. Clone the repository
git clone https://github.com/mohanthakur-dev/CampusFlow.git
2. Open the project
cd CampusFlow
3. Install dependencies
pip install -r requirements.txt
4. Start the Flask application
python3 app.py
5. Open in your browser
http://127.0.0.1:5000
🎯 Why CampusFlow?
College work is often scattered across different places:
WhatsApp messages
Classroom announcements
PDFs
Notes
Lab records
Previous papers
Different websites
CampusFlow brings these academic tasks and resources together into one simple workspace.
The goal is to make it easier for students to know:
What do I need to do, when do I need to do it, and where is the resource I need?
🔮 Future Plans
CampusFlow is planned to become more intelligent and convenient.
🤖 AI Task Extraction
Users will be able to paste a college announcement such as:
DBMS assignment 3 needs to be submitted by 15 October.
CampusFlow will extract useful information such as:
Subject: DBMS
Type: Assignment
Title: Assignment 3
Deadline: 15 October
Status: Pending
The user will be able to review and confirm before saving the task.
🎙️ Voice Input
Future versions will support voice input so students can add tasks without typing everything manually.
For example:
"DBMS assignment 15 October ko submit karna hai."
The system can convert the voice input into a structured task.
🔎 Smart Search
Future versions may include intelligent search across:
Assignments
Notes
Resources
Class updates
Previous papers
🗄️ Production Database
The current version uses SQLite.
A future production version will use PostgreSQL for more reliable persistent data storage.
📱 Mobile Experience
The interface will continue to be improved for mobile devices.
📌 Project Status
V1 — Live 🚀
The core CampusFlow features are implemented and deployed.
Future versions will focus on AI-powered organization, voice input, smarter search, and improved data persistence.
👨‍💻 Author
Mohan Thakur
GitHub:
https://github.com/mohanthakur-dev⁠
⭐ Support
If you find the project interesting, consider giving the repository a ⭐ on GitHub.