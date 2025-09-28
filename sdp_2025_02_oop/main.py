from collections.abc import Iterable

from dao.idgen_autoincrement import IdGenAutoincrement
from dao.idgen_uuid import IdGenUuid
from dao.repository_inmemory import RepositoryInMemory
from dao.repository_jsonfile import RepositoryJsonFile
from dao.student_repository_inmemory import StudentRepositoryInMemory
from dao.student_repository_jsonfile import StudentRepositoryJsonFile
from model.answer import Answer
from model.instructor import Instructor
from model.person import Person
from model.question import Question, QuestionType
from model.student import Student
from model.test import Test


def print_persons(persons: Iterable[Person]):
    for person in persons:
        print(str(person))


if __name__ == '__main__':
    # trayan = Instructor('Trayan Iliev', 'Sofia 1000', '0887453214', 'trayan@gmail.com',
    #                     '', '305', courses= ['UP', 'SDP', 'IA with Gen AI'])
    # george = Student('George', fn='0PH23235', semester=1)
    # ana = Student('Ana', fn='0MI123456', semester=2)

    # print('Persons:')
    student_repo = StudentRepositoryJsonFile('students.json', IdGenUuid())

    # person_repo.add(trayan)
    # student_repo.add(george)
    # student_repo.add(ana)
    print('BEFORE - Num students:', len(student_repo))
    print_persons(student_repo.find_all())
    print('AFTER - Num students:', len(student_repo))

    test_repo = RepositoryJsonFile('tests.json', IdGenUuid())
    test_repo.add(Test('Python Programming', [
        Question('Does Python support multiple inheritance?',
                 [
                     Answer('Yes', 1, id=0),
                     Answer('No', 0, id=1),
                 ], id=0),
        Question('Which types are immutable in Python',
                 [
                     Answer('str', 1, id=0),
                     Answer('int', 1, id=1),
                     Answer('list', 0, id=2),
                     Answer('dict', 0, id=3),
                     Answer('set', 0, id=4),
                     Answer('tuple', 1, id=5),
                 ], type=QuestionType.MULTIPLE_RESPONSE, id=0),
        Question('Are there interfaces in Python?',
                 [
                     Answer('Yes', 0, id=0),
                     Answer('No', 1, id=1),
                 ], id=0),
        Question('Which method allows to merge two lists in Python?',
                 [
                     Answer('append', 0, id=0),
                     Answer('extend', 1, id=1),
                     Answer('insert', 0, id=2),
                 ], id=0),
    ], minutes=20))
    test1 = test_repo.find_all()[0]
    # test1.questions.sort(key=lambda q: q.text.lower())
    questions_sorted = sorted(test1.questions, key=lambda q: q.text.lower())
    for question in questions_sorted:
        print(question)
