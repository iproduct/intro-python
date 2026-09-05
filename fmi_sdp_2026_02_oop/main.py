from dao.UserRepository import UserRepository
from dao.id_generator import IdGeneratorUuid
from model.user import User


def print_users(users):
    for u in users:
        print(f'| {str(u.id)[-12:]:12.12s} | {u.username:12.12s} | {u.fname + ' ' + u.lname:20.20s} '
              f'| {u.email:20.20s} | {u.password:12.12s} | {','.join(u.roles):20.20s} |')


if __name__ == "__main__":
    id_gen = IdGeneratorUuid()
    user_repo = UserRepository(id_gen)
    u1 = user_repo.create(User(fname="John", lname="Doe", email="john@gmail.com",
                      username="john", password="john123", roles=["user", "admin"]))
    print(f'Created user: {u1}')
    u2 = user_repo.create(User(fname="Jane", lname="Smith", email="jane@gmail.com",
                      username="jane", password="jane123", roles=["manager", "admin"]))
    u3 = user_repo.create(User(fname="Hristo", lname="Dimitrov", email="hristo@gmail.com",
                      username="hristo", password="hristo123", roles=["user"]))

    users = user_repo.find()
    print_users(users)
