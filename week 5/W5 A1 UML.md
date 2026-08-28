
#Use Case Diagram
Student: enroll_course, submit_assignment, view_grades, view_course_info
Lecturer:  view_students, give_grades, view_course_info

![alt text](image.png)

#Activities Diagram
Student can view the courses information and enroll the course they want. After enroll a course, they can submit their assignments.
Lecturer can view all students and give grades for every assignments. 
The Student can view their grade.

學生先查看課程資訊並選擇是否註冊課程。完成註冊後，學生提交作業，系統儲存提交內容並通知 Lecturer。Lecturer 查看學生與作業後給予成績，系統再儲存成績，最後 Student 可以查看自己的 Grade。

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


UC Diagram:
https://www.planttext.com?text=RP9DImCn48RlWVo7OUyzs2zlKbca27fQz3xkJjFGR5AIYLB4_sx2xYfDDxUyyymx7yakC7gElP4YdBGzeySUpjYUK5735qFWgMMqof0KXWuCxC1hTMJeT0vfPwMG0bjs7XgE7LcUhYyf7Ztv3FpPG5KxOqWHlA9DLVgK0CqbCFKLV4i1wSH0BOQ4FbcVOAXTz84gm01lzLt1DF6ZrmoF8MXbizl8BGlkNTCNx3rs54PYDKSCjU3P7jo8hGjiw7i6tCpvZJkPQcuBPgy_wRghUob-yiR6H5Wi7eQfhuLbAQnAOPrTfZVurmfbSwDiRvJKqevibxx9Bm00

Class Diagram:
https://www.planttext.com?text=ZLCxJiGm4EqZvGwZD6I1hA1DWLQYeA620qJUP3POIcnaJvO2KI11nG4G2D5IGeKuKO1RhDVvQxE85B4yxysyDsDxfeafAlBCTUACQGtdL2Ge2AvT1ymNWAu24Kz20oekqWOHBCTXR0zGA9bbKImBfT6lbX2ExJe9OIbvqb1rCSyvHKQKfo8t4d_JbnolebIn1FqMkN6TnlSfnbGeL9tnh8xyqtdAbrZNj_ypZAKocIVhpJveisjpngnLvYCk5d9R8psx5TAPRR8thDO0SSesBICDP2STeITb6-YKR7CZGjlFUQktmKpwfjfZ6aB5PS888vlcZm_K-jw1ykk-VFhuVhxxVNpvkNqlNp_BjmVNQIwdT-X1481tC9tkUdM38SWvCIuq7BbEFTvnNYo5vfeqoCMQszwS8Rik4G8XYo_GbfsXICnRMG40

https://www.planttext.com?text=RL7BQiCm4BmR_0zxJ0xz0VMGXBI4G9j31OKULNljBkXHf9MBmHzVIRQRjFGaxSxipAoq3wmyHwFhYearmj557n2UbLKz6hGCSWoC1kxWq30Dn2CyaEgzCdLLLvFas2RMb8kYbI_YbV1hbJhRpdcZc9ozpo1ri7cqtcaDPA4ffDqM-0CjRDumREiAG4ZKsF2YKUO0fZdAL0YBnEAVfNwu2Jqwsv4tCBFo7gcFjgNkJseXuxiXXaC8rDk5c1chbP1gm1iOoa0gophYufYw4PvIsEZHpyDhDQrFiVY5FF62GsxzCXGdIYOdhrhyr_uMkKOlqbSeiFlCvpxjcNxq6m00
