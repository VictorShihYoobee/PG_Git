# week 3/Act 4 project/user_manager.py
from database import *
import sqlite3

# Function to add a new student to the database
def add_user(nid, name, email, B_date, Phone_number):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Student (NID, F_name, L_name, Email, B_date, Phone_number) VALUES (?, ?, ?, ?, ?, ?)",
                       (nid, name, email, B_date, Phone_number))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

# Function to view all students in the database
def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to search for students by name
def search_student(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student WHERE F_name LIKE ?",
                   ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to delete a student by NID
def delete_student(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Student WHERE NID = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted.")

# Function to show the contents of any table
def show_table_contents(table_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to show the count of students per course
def show_student_count_per_course():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT Course_name, COUNT(DISTINCT Student_code) AS Total_Students
        FROM Enrollment
        GROUP BY Course_name;
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to show students with multiple courses
def show_students_with_multiple_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT 
            s.NID AS Student_ID, 
            s.F_name || ' ' || s.L_name AS Full_Name, 
            COUNT(e.CC_num) AS Enrolled_Courses_Count
        FROM 
            Student s
        JOIN 
            Enrollment e ON s.NID = e.Student_code
        GROUP BY 
            s.NID, s.F_name, s.L_name
        HAVING 
            COUNT(e.CC_num) > 1;
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return rows