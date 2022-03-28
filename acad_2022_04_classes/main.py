from dao.id_generator_int import IdGeneratorInt
from dao.id_generator_uuid import IdGeneratorUuid
from dao.repository import Repository
from entity.person import Person


def print_all_persons(repo):
    print()
    for p in repo.find_all():
        print(p.get_formatted_str())
    print(f'Number of persons: {len(repo)}')


if __name__ == '__main__':
    p1 = Person('Ivan', 'Petrov', 25)
    p2 = Person('Dimitar', 'Hristov', 35)
    p3 = Person('Maria', 'Georgieva', 27)
    persons = [p1, p2, p3]

    id_gen = IdGeneratorUuid()
    persons_repo = Repository(id_gen)
    for p in persons:
        persons_repo.create(p)
    print_all_persons(persons_repo)

    # second: Person = persons_repo.find_by_id(2)
    # second.f_name = 'Mitko'
    # persons_repo.update(second)
    # persons_repo.delete_by_id(1)
    # print_all_persons(persons_repo)

    other_repo = Repository(id_gen)
    other_repo.create(Person('John', 'Smith', 39))
    other_repo.create(Person('Johanna', 'Harrison', 27))
    print_all_persons(other_repo)

    persons_repo += other_repo
    print_all_persons(persons_repo)