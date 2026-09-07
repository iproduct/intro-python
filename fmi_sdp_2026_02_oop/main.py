from typing import Iterable

from dao.id_generator import IdGeneratorUuid
from dao.user_repository_memory_impl import UserRepositoryMemoryImpl
from model.customer import Customer
from model.user import User


def print_users[IDType](users: Iterable[User[IDType]]):
    for usr in users:
        print(f'| {str(usr.id)[-12:]:12.12s} | {str(usr.username):12.12s} | {(str(usr.fname) + ' ' + str(usr.lname)):20.20s} '
              f'| {str(usr.email):20.20s} | {str(usr.password):20.20s} | {','.join(usr.roles):20.20s} |')


if __name__ == "__main__":
    id_gen = IdGeneratorUuid()
    user_repo = UserRepositoryMemoryImpl(id_gen)
    u1 = user_repo.create(User(fname="John", lname="Doe", email="john@gmail.com",
                               username="john", password="john123", roles=["user", "admin"]))
    print(f'Created user: {u1}')
    u2 = user_repo.create(Customer(fname="Jane", lname="Smith", email="jane@gmail.com",
                                   username="jane", password="jane123", address='London'))
    u3 = user_repo.create(Customer(fname="Hristo", lname="Dimitrov", email="hristo@gmail.com",
                                   username="hristo", password="hristo123", phone='+359885324567'))
    # user_repo.create('Trayan')

    users = user_repo.find()
    print_users(users)
    u4 = user_repo.find_by_id(u2.id)
    if u4 is not None:
        u4.password = "modified123"
        # setattr(u4, 'password', "modified123")
        user_repo.update(u4)
    users = user_repo.find()
    # user_repo.delete(u3.id)
    print_users(users)
    print(f'Users in repository: {len(user_repo)}')
    for u in user_repo:
        print(u.__repr__())
