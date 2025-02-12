from model.person import Person

class Instructor(Person):
    def __init__(self, name = None, address = None, phone = None, email = None, degree= '', room = None,
                 courses = None, iid = None):
        super().__init__(name, address, phone, email, iid)
        self.degree = degree
        self.room = room
        self.courses = courses if courses is not None else []

    def change_semester(self, new_semester):
        self.semester = new_semester

    def __str__(self):
        return f'{super().__str__()}, {f"Degree: {self.degree}, " if self.degree else ""}Room:{self.room}, Course: {self.courses}'

    def __repr__(self):
        return (f'Instructor(ID: {self.id}, Degree: {self.degree}, Name: {self.name}, FN:{self.room}, '
                f'Courses: {self.courses})')
