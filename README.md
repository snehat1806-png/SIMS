# 🎓 Student Information Management System (SIMS)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Storage](https://img.shields.io/badge/Storage-JSON-green.svg)
![Platform](https://img.shields.io/badge/Platform-CLI-orange.svg)
![Status](https://img.shields.io/badge/Status-Stable-success.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

A professional **Command Line Student Information Management System** built using Python and JSON storage.
This application allows efficient management of student records with persistent storage, structured data handling, and clean modular design.

---

# 📌 Overview

The Student Information Management System (SIMS) is designed to manage student records efficiently using modern JSON-based storage instead of traditional text files.

This project demonstrates:

* File handling with JSON
* CRUD operations
* Data persistence
* Modular Python programming
* Git version control and project structuring

---

# ✨ Features

* ➕ Add new student
* 👁️ View student by ID
* 📋 List all students
* 🔍 Search student by name
* ✏️ Update student details
* 🗑️ Soft delete student
* 💾 Persistent JSON storage
* 🕒 Timestamp tracking
* 🧱 Clean project structure

---

# 🏗️ System Architecture

```text
User (CLI)
   │
   ▼
main.py (Application Logic)
   │
   ▼
JSON Handler Functions
   │
   ▼
students.json (Database)
```

---

# 🗂️ Project Structure

```text
Student Information Management System/
│
├── main.py
├── students.json
├── README.md
├── .gitignore
│
├── DeletedStudents/
│
└── .github/
```

---

# ⚙️ Technologies Used

| Technology | Purpose                 |
| ---------- | ----------------------- |
| Python 3   | Core programming        |
| JSON       | Data storage            |
| Git        | Version control         |
| GitHub     | Remote repository       |
| VS Code    | Development environment |

---

# ▶️ Installation & Usage

## 1️⃣ Clone repository

```bash
git clone https://github.com/snehat1806-png/SIMS.git
```

## 2️⃣ Navigate to folder

```bash
cd SIMS
```

## 3️⃣ Run program

```bash
python main.py
```

---

# 🖥️ Application Menu

```text
===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. View Student
3. List Students
4. Search by Name
5. Update Student
6. Delete Student
7. Exit
```

---

# 💾 JSON Database Example

```json
[
  {
    "id": 101,
    "name": "Sneha Tiwari",
    "department": "CSE",
    "year": "3",
    "email": "sneha@email.com",
    "phone": "9876543210",
    "status": "ACTIVE",
    "createdAt": "2026-02-28 17:00:00",
    "lastUpdated": "2026-02-28 17:00:00"
  }
]
```

---

# 🔄 Migration Improvement

This project was upgraded from:

Text file storage (.txt) ❌
to
JSON structured storage (.json) ✅

Benefits:

* Better performance
* Structured data
* Easier updates
* Industry-standard approach
* Scalable architecture

---

# 🧠 Concepts Demonstrated

* File handling
* JSON data management
* CRUD operations
* Modular programming
* CLI application design
* Git branching and rebasing
* Project restructuring

---

# 🚀 Future Enhancements

* GUI version (Tkinter)
* SQLite / MySQL database integration
* REST API (Flask / FastAPI)
* Web interface
* User authentication

---

# 📊 Version History

| Version | Storage | Description              |
| ------- | ------- | ------------------------ |
| 1.0     | TXT     | File-based storage       |
| 2.0     | JSON    | Migrated to JSON storage |

---

# 👩‍💻 Author

**Sneha Tiwari**

GitHub:
https://github.com/snehat1806-png

---

# ⭐ Resume Value

This project demonstrates real-world skills in:

* Python development
* Data management
* Software architecture
* Git version control
* Project migration and restructuring

---

# 📄 License

This project is open source and available under the MIT License.
