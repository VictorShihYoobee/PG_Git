class Lecturer:
    def __init__(self, lecturer_id, name):
        self.lecturer_id = lecturer_id
        self.name = name

    def give_grade(self, grade_record, grade):
        grade_record.update_grade(grade)

    def view_course_info(self, course):
        return course.get_course_info()