from xml.dom.minidom import Entity

from dao.abstract_repository import AbstractRepository
from dao.repository_memory_Impl import RepositoryMemoryImpl
from dao.user_repository import UserRepository
from exception.non_exisiting_entity_exception import NonExistingEntityException
from model.user import User


class UserRepositoryMemoryImpl[IDType](RepositoryMemoryImpl[IDType, User[IDType]], UserRepository[IDType]):
    pass

