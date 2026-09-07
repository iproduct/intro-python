from dao.repository_memory_Impl import RepositoryMemoryImpl
from dao.user_repository import UserRepository
from model.user import User


class UserRepositoryMemoryImpl[IDType](RepositoryMemoryImpl[IDType, User[IDType]], UserRepository[IDType]):
    pass

