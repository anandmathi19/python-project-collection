# ☕ Cafe API (Flask + SQLAlchemy)

A simple REST API built with **Flask** and **SQLite** that provides information about cafes such as location, WiFi availability, seating, and coffee prices.

This project is part of my Python backend learning journey.

---

## 🚀 Features

* Get a random cafe
* View all cafes
* Search cafes by location
* JSON API responses
* SQLite database
* Flask + SQLAlchemy ORM

---

## 🛠 Tech Stack

* Python
* Flask
* SQLAlchemy
* SQLite
* HTML

---

## 📂 Project Structure

```
project-folder
│
├── app.py
├── cafes.db
├── templates
│   └── index.html
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository

```
git clone https://github.com/yourusername/cafe-api.git
```

2. Move into the project folder

```
cd cafe-api
```

3. Install dependencies

```
pip install flask flask_sqlalchemy
```

4. Run the application

```
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

### Get Random Cafe

```
/random
```

### Get All Cafes

```
/all
```

### Search Cafe By Location

```
/search?loc=Peckham
```

Example:

```
http://127.0.0.1:5000/search?loc=Clerkenwell
```

## 👨‍💻 Author

Ananda Raj
B.Tech Artificial Intelligence & Data Science Student

Learning backend development and working toward becoming an AI Engineer.
