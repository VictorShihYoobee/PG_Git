class Grade:
    def __init__(self, grade_id, course_id, student_id, grade=None):
        self.grade_id = grade_id
        self.course_id = course_id
        self.student_id = student_id
        self.grade = grade

    def update_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade