# CampusFlow

> One place to manage everything that college throws at you.

CampusFlow is a college productivity and academic management web application designed to keep assignments, lab records, study resources, class updates, deadlines, and previous question papers organized in one place.

Instead of managing college work across different notebooks, messages, and files, CampusFlow provides a single dashboard to keep track of everything.

---

## 🚀 Features

### 📊 Dashboard
- View total assignments
- Track pending and completed assignments
- View lab record statistics
- See upcoming deadlines
- View upcoming assignments and lab records
- See the latest class update
- Quick access to important sections

### 📚 Assignments
- Add new assignments
- Add subject and deadline
- Track pending/completed status
- Mark assignments as completed
- Delete assignments

### 🧪 Lab Records
- Add lab experiments
- Add subject and deadline
- Track pending/completed status
- Mark records as completed
- Delete lab records

### 📄 Notes & Resources
- Store study resources
- Add subject and title
- Select resource type
- Store resource links
- Delete resources when no longer needed

### 📢 Class Updates
- Add class announcements
- Store title, message, and date
- View the latest class update directly from the dashboard
- Delete old updates

### 📅 Deadlines
- Combined view of assignment and lab deadlines
- Pending work is displayed in one place
- Deadlines are sorted by date

### 📝 Previous Papers
- Store previous question papers
- Add subject, year, semester, and exam type
- Store paper links
- Delete papers

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| HTML | Page structure |
| CSS | Styling and UI |
| JavaScript | Frontend interactions |
| Python | Backend programming |
| Flask | Web framework |
| SQLite | Database |

---

## 📁 Project Structure

```text
CampusFlow/
│
├── app.py
├── campusflow.db
├── README.md
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