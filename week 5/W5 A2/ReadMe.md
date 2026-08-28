Week 5 - Activity 2: Develop the OOP
Based on designed ER and UML diagrams, develop the OOP project for (College project) as a CLI


#Use Case Diagram
Student: enroll_course, submit_assignment, view_grades, view_course_info
Lecturer:  view_students, give_grades, view_course_info

![alt text](image.png)

#Activities Diagram
Student can view the courses information and enroll the course they want. After enroll a course, they can submit their assignments.
Lecturer can view all students and give grades for every assignments. 
The Student can view their grade.

![alt text](image-2.png)

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

![alt text](image-3.png)

