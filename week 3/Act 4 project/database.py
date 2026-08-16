# week 3/Act 4 project/database.py
import sqlite3

# Function to create a database connection
def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

# Function to create tables in the database
def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    # Enable Foreign Key constraints in SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Student Entity
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Student (
                Student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                NID TEXT GENERATED ALWAYS AS ('STU' || PRINTF('%03d', Student_id)) STORED UNIQUE,
                F_name TEXT NOT NULL,
                L_name TEXT NOT NULL,
                B_date DATE,
                Email TEXT,              -- Added Attribute
                Phone_number TEXT        -- Added Attribute
            );
        """
    )

    # 2. Lecturer Entity
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Lecturer (
                Lecture_id TEXT PRIMARY KEY,
                L_firstname TEXT NOT NULL,
                L_lastname TEXT NOT NULL,
                L_email TEXT,              -- Added Attribute
                L_phone TEXT,              -- Added Attribute
                L_address TEXT
            );
        """
    )

    # 3. Subjects Entity
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Subjects (
                Subject_code TEXT PRIMARY KEY,
                Subject_unit INTEGER NOT NULL,
                Subject_udsc TEXT,
                Credits INTEGER DEFAULT 15        -- Added Attribute
            );
        """
    )

    # 4. Lecture Entity
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Lecture (
                CC_num TEXT PRIMARY KEY,         -- CC# from ER diagram
                Lecture_name TEXT NOT NULL,
                Date DATE,
                Time TIME,
                Subject_code TEXT NOT NULL,
                Lecture_id TEXT NOT NULL,
                Room_number TEXT,                -- Added Attribute
                FOREIGN KEY (Subject_code) REFERENCES Subjects(Subject_code) 
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (Lecture_id) REFERENCES Lecturer(Lecture_id) 
                    ON DELETE CASCADE ON UPDATE CASCADE
            );
        """
    )

    # 5. Enrollment Entity (Junction / Relationship Table)
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Enrollment (
                Enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                Student_code TEXT NOT NULL,       -- Foreign Key to Student (NID)
                CC_num TEXT NOT NULL,             -- Foreign Key to Lecture (CC#)
                Date_of_enrollment DATE NOT NULL,
                Course_name TEXT NOT NULL,
                Grade TEXT,                       -- Added Attribute
                Status TEXT DEFAULT 'Active',     -- Added Attribute
                FOREIGN KEY (Student_code) REFERENCES Student(NID) 
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (CC_num) REFERENCES Lecture(CC_num) 
                    ON DELETE CASCADE ON UPDATE CASCADE
            );
        """
    )

    conn.commit()
    conn.close()
    print("Database schema created successfully.")

# Function to populate the database with sample data
def populate_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Insert 3 Subjects (Courses)
    subjects = [
        (
            "MSE800",
            15,
            "Professional Software Engineering",
            15,
        ),  # Subject_code, Subject_unit, Subject_udsc, Credits
        ("MSE801", 15, "Research Methods", 15),
        ("MSE802", 15, "Advanced Database Systems", 15),
    ]

    cursor.executemany(
        """
        INSERT OR IGNORE INTO Subjects (Subject_code, Subject_unit, Subject_udsc, Credits)
        VALUES (?, ?, ?, ?);
    """,
        subjects,
    )

    # 2. Insert 2 Lecturers
    lecturers = [
        (
            "LEC01",
            "Mohammad",
            "Norouzifard",
            "mohammad.n@yoobee.ac.nz",
            "Auckland"
        ),
        (
            "LEC02",
            "Debnath",
            "Shukla",
            "debnath.s@yoobee.ac.nz",
            "Auckland"
        ),
    ]

    cursor.executemany(
        """
        INSERT OR IGNORE INTO Lecturer (Lecture_id, L_firstname, L_lastname, L_email, L_address)
        VALUES (?, ?, ?, ?, ?);
    """,
        lecturers,
    )

    # 3. Insert 5 Students
    students = [
        (
            "Daniel",
            "Banggawan",
            "2002-05-14",
            "daniel@student.ac.nz",
            "021111111",
        ),
        (
            
            "Choonho",
            "Lee",
            "2000-08-22",
            "choonho@student.ac.nz",
            "022222222",
        ),
        (
            
            "Chaw",
            "Theingi",
            "2001-11-03",
            "chaw@student.ac.nz",
            "023333333",
        ),
        (
            
            "Sukhjeet",
            "Singh",
            "1999-03-19",
            "sukhjeet@student.ac.nz",
            "024444444",
        ),
        (
            
            "Smriti",
            "Bhandari",
            "2001-01-30",
            "smriti@student.ac.nz",
            "025555555",
        ),
    ]

    cursor.executemany(
        """
        INSERT OR IGNORE INTO Student ( F_name, L_name, B_date, Email, Phone_number)
        VALUES (?, ?, ?, ?, ?);
    """,
        students,
    )

    # 4. Insert Lecture Sessions (linking Courses & Lecturers)
    lectures = [
        (
            "CC101",
            "Software Architecture & Design",
            "2026-08-20",
            "09:00:00",
            "MSE800",
            "LEC01",
            "Lab 1",
        ),
        (
            "CC102",
            "Research Methodologies",
            "2026-08-21",
            "11:00:00",
            "MSE801",
            "LEC02",
            "Lab 2",
        ),
        (
            "CC103",
            "SQL & Relational Modeling",
            "2026-08-22",
            "14:00:00",
            "MSE802",
            "LEC01",
            "Lab 3",
        ),
    ]

    cursor.executemany(
        """
        INSERT OR IGNORE INTO Lecture (CC_num, Lecture_name, Date, Time, Subject_code, Lecture_id, Room_number)
        VALUES (?, ?, ?, ?, ?, ?, ?);
    """,
        lectures,
    )

    # 5. Insert Enrollment Records
    enrollments = [
        (
            "STU001",
            "CC101",
            "2026-08-01",
            "Professional Software Engineering",
            "A",
            "Active",
        ),
        (
            "STU001",
            "CC102",
            "2026-08-01",
            "Research Methods",
            "A-",
            "Active",
        ),  # Student 1 enrolled in >1 course
        (
            "STU002",
            "CC101",
            "2026-08-01",
            "Professional Software Engineering",
            "B+",
            "Active",
        ),
        (
            "STU002",
            "CC103",
            "2026-08-01",
            "Advanced Database Systems",
            "A",
            "Active",
        ),  # Student 2 enrolled in >1 course
        (
            "STU003",
            "CC102",
            "2026-08-02",
            "Research Methods",
            "B",
            "Active",
        ),
        (
            "STU004",
            "CC103",
            "2026-08-02",
            "Advanced Database Systems",
            "A+",
            "Active",
        ),
        (
            "STU005",
            "CC101",
            "2026-08-03",
            "Professional Software Engineering",
            "A",
            "Active",
        ),
    ]

    cursor.executemany(
        """
        INSERT INTO Enrollment (Student_code, CC_num, Date_of_enrollment, Course_name, Grade, Status)
        VALUES (?, ?, ?, ?, ?, ?);
    """,
        enrollments,
    )

    conn.commit()
    conn.close()
    print("Sample data populated successfully.")

if __name__ == "__main__":
    create_table()
    populate_database()