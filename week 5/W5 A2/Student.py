class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def submit_assignment(self, assignment):
        return f"{self.name} submitted {assignment}"

    def enroll_course(self, course):
        return f"{self.name} enrolled in {course.course_title}"

    def view_grade(self, grade):
        return grade.get_grade()