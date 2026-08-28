class Course:
    def __init__(self, course_id, course_title):
        self.course_id = course_id
        self.course_title = course_title

    def get_course_info(self):
        return f"{self.course_id}: {self.course_title}"