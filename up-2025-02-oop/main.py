from collections.abc import Iterable

from dao.idgen_autoincrement import IdGenAutoincrement
from dao.repository_inmemory import RepositoryInMemory
from dao.student_repository_inmemory import StudentRepositoryInMemory
from model.instructor import Instructor
from model.person import Person
from model.student import Student

def print_persons(persons: Iterable[Person]):
    for person in persons:
        print(str(person))

if __name__ == '__main__':
    # trayan = Instructor('Trayan Iliev', 'Sofia 1000', '0887453214', 'trayan@gmail.com',
    #                     '', '305', courses= ['UP', 'SDP', 'IA with Gen AI'])
    george = Student('George', fn='0PH23235', semester=1)
    ana = Student('Ana', fn='0MI123456', semester=2)

    # print('Persons:')
    person_repo = RepositoryInMemory(IdGenAutoincrement())
    # person_repo.add(trayan)
    person_repo.add(george)
    person_repo.add(ana)
    print('Num students:', len(person_repo))
    # print_persons(person_repo.find_all())

    # print('Instructors:')
    # instructor_repo = RepositoryInMemory(IdGenAutoincrement())
    # instructor_repo.add(trayan)
    # print_persons(instructor_repo.find_all())
    #
    # print('\nStudents:')
    # student_repo = StudentRepositoryInMemory(IdGenAutoincrement())
    # student_repo.add(george)
    # student_repo.add(ana)
    # print_persons(student_repo.find_all())
    # fn = '0PH23235'
    # print(f'\nFN: {fn} -> {student_repo.find_by_fn(fn)}')
    # print(trayan in student_repo)
    # print('\nStudents using iterator:')
    for student in person_repo:
        print(student)

    print(person_repo.find_by_id(1).__dict__, '\n')
    print(Student.__dict__)
    print(Student.__annotations__)

    # d = {}
    # print(d['a'])
