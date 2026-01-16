# Phase 4 Flask Code Challenge

## Overview

This project is a Flask REST API built for the Phase 4 Code Challenge. It demonstrates understanding of models, relationships, validations, RESTful routing, and structured JSON responses using Flask, SQLAlchemy, and Flask-Migrate.

The goal is to implement the **minimum required functionality** correctly and cleanly so that all rubric criteria are met.

---

## Tech Stack

* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* SQLite

---

## Project Structure

```
code-challenge/
├── app.py
├── config.py
├── models.py
├── routes.py
├── seed.py
├── requirements.txt
├── README.md
├── instance/
│   └── app.db
├── migrations/
└── tests/
```

---

## Setup Instructions

1. Clone or unzip the project folder
2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set environment variables

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

5. Initialize the database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

---

## Running the Server

```bash
python app.py
```

The server will run on:

```
http://127.0.0.1:5555
```

---

## API Behavior

* All routes follow RESTful naming conventions
* All responses are returned in JSON format
* Appropriate HTTP status codes are used for success and error cases
* Relationships are serialized using nested JSON where required

---

## Database

* SQLite is used for simplicity
* Migrations are handled using Flask-Migrate
* Models include validations to enforce data integrity

---

## Testing

Manual testing can be done using:

* Browser
* Postman
* curl

Run the server and hit the available endpoints to confirm responses and status codes.

---

## Submission Instructions

1. Ensure all changes are committed

```bash
git add .
git commit -m "Complete Phase 4 Code Challenge"
```

2. Navigate to the parent directory and run:

```bash
./bin/end.py
```

3. Upload the generated `.bundle` file to Canvas

---

## Author

Alex Mureti Maingi
