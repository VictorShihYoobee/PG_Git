Week 5 - Activity 2: Develop the OOP
Based on designed ER and UML diagrams, develop the OOP project for (College project) as a CLI


#Use Case Diagram
Student: enroll_course, submit_assignment, view_grades, view_course_info
Lecturer:  view_students, give_grades, view_course_info

<img width="359" height="509" alt="image" src="https://github.com/user-attachments/assets/fc21114c-ec3b-4126-b07b-61b07d49224d" />


#Activities Diagram
Student can view the courses information and enroll the course they want. After enroll a course, they can submit their assignments.
Lecturer can view all students and give grades for every assignments. 
The Student can view their grade.

<img width="587" height="889" alt="image-2" src="https://github.com/user-attachments/assets/9a464c36-b7ab-464a-908d-5e7ae830d079" />


#Class Diagram
Student: student_id, name

    + submit_assignment

    + enroll_course
    
    + view_grade

Lecturer: lecturer_id, name
    
    + give_grade
    
    + view_course_info

Course: course_id, course_title
    
    + get_course_info

grades: grade_id, course_id, student_id, grade
    + update_grade
    + get_grade

<img width="382" height="543" alt="image-3" src="https://github.com/user-attachments/assets/ad7b54a7-db83-406e-bb80-c72b6f006ad6" />


