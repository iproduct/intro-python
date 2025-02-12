from collections.abc import Iterable

from dao.idgen_autoincrement import IdGenAutoincrement
from dao.repository_inmemory import RepositoryInMemory
from model.instructor import Instructor
from model.person import Person
from model.student import Student

def print_persons(persons: Iterable[Person]):
    for person in persons:
        print(str(person))

if __name__ == '__main__':
    trayan = Instructor('Trayan Iliev', 'Sofia 1000', '0887453214', 'trayan@gmail.com',
                        '', '305', courses= ['UP', 'SDP', 'IA with Gen AI'])
    george = Student('George', fn='0PH23235', semester=1)
    uni_persons = [trayan, george]
    print_persons(uni_persons)

    person_repo = RepositoryInMemory(IdGenAutoincrement())
    person_repo.find_all()

