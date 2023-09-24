from model.instructor import Instructor, print_instructors
from persistable import Persistable
from repository import Repository

class InstructorRepository(Repository, Persistable):
    def __init__(self, initial_instructors_list=None, file_name='instructors.json'):
        Repository.__init__(self, initial_instructors_list)
        Persistable.__init__(self, file_name, Instructor)
    def find_by_department(self, department):
        return [i for i in self.find_all() if i.department == str(department)]

    def find_by_name(self, name_part):
        return [i for i in self.find_all() if name_part.lower() in i.name.lower()]

    def find_by_course(self, course_part):
        results = []
        for instr in self.find_all():
            for c in instr.courses:
                if course_part.lower() in c.lower():
                    results.append(instr)
                    break
        return results

if __name__ == '__main__':
    instructors = [
        Instructor('Georgi Petrov', '23.07.1999', 'IT', ['UP', 'SDP'], '01.09.2010'),
        Instructor('Hristina Dimitrova', '07.05.2005', 'IT', ['UP', 'SDP'], '01.03.2015'),
        Instructor('Ivan Genov', '21.09.1982', 'IT', ['UP'], '01.07.2003'),
        Instructor('Georgi Genov', '21.09.1982', 'SE', ['UP', 'SDP', 'Python'], '01.07.2003'),
    ]
    repo = InstructorRepository(instructors, 'instructors.json')

    print(repo.find_by_id(2))
    print()
    print_instructors(repo.find_by_name('Georgi'))
    print()
    print_instructors(repo.find_by_department('IT'))

    print()
    print(repo.find_by_id(2).id)

    print()
    print_instructors(repo.find_by_course('P'))

    # repo.save()
    #
    # repo_from_file = InstructorRepository()
    # repo_from_file.load()
    # print('\nAFTER READING FROM FILE:')
    # print_instructors(repo_from_file.find_all())

