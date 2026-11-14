# PostgreSQL CRUD Application

A Python application that connects to a PostgreSQL database and performs CRUD (Create, Read, Update, Delete) operations on a `students` table.

## Demo Video
https://youtu.be/JPA69O1OSUs 


## Project Structure

```
├── app/
│   └── main.py                # Python application with the four CRUD functions
├── database/
│   └── student_schema.sql     # Creates the students table and inserts the initial data
└── README.md
```

## Functions

| Function | Operation | Description |
|---|---|---|
| `getAllStudents()` | Read | Retrieves and prints all records from the `students` table |
| `addStudent(first_name, last_name, email, enrollment_date)` | Create | Inserts a new student record |
| `updateStudentEmail(student_id, new_email)` | Update | Updates the email of the student with the given ID |
| `deleteStudent(student_id)` | Delete | Deletes the student with the given ID |

## Used

- Python 3
- PostgreSQL
- pgAdmin
- The `psycopg2-binary` library

## Setup and Run Instructions

### 1. Create the database

1. Open pgAdmin and create a new database (for example, `student_db`).
2. Open the Query Tool on that database.
3. Open `database/schema.sql`, paste it into the Query Tool, and run it.
   This creates the `students` table and inserts the initial 3 students.

### 2. Install the library

From the project folder, run:

```
pip install psycopg2-binary
```

(Optional: create a virtual environment first with `python3 -m venv .venv` and activate it with `source .venv/bin/activate`.)

### 3. Configure the connection

Open `app/main.py` and edit `DB_CONFIG` at the top to match your PostgreSQL setup:

```python
DB_CONFIG = {
    "dbname": "student_db",       # the database you created in pgAdmin
    "user": "postgres",           # your PostgreSQL username
    "password": "your_password",  # your PostgreSQL password
    "host": "localhost",
    "port": "5432",
}
```

### 4. Run the application

```
python3 main.py
```

The program runs a demo that calls each function in order:

1. Prints all students
2. Adds a new student
3. Updates a student's email
4. Deletes a student

You can check each change in pgAdmin by right-clicking the `students` table and choosing **View/Edit Data > All Rows**.
