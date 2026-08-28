#!/usr/bin/env python3
"""
Simple Course Management System
"""

from Student import Student
from Lecturer import Lecturer
from Course import Course
from Grades import Grade

student = Student(1, "Victor")
lecturer = Lecturer(1, "John")
course = Course(101, "Software Engineering")
grade = Grade(1, 101, 1)

while True:
    print("\n--- Course Management System ---")
    print("1. Enrol student in course")
    print("2. Submit assignment")
    print("3. Give grade for student")
    print("4. View grades")
    print("5. View course info")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(student.enroll_course(course))

    elif choice == "2":
        assignment = input("Enter assignment name: ")
        print(student.submit_assignment(assignment))

    elif choice == "3":
        new_grade = float(input("Enter grade: "))
        lecturer.give_grade(grade, new_grade)
        print("Grade updated.")

    elif choice == "4":
        grades = student.view_grade(grade)
        print(grades)

    elif choice == "5":
        print(lecturer.view_course_info(course))

    elif choice == "6":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")