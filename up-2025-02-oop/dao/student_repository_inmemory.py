from dao.id_generator import IdGenerator
from dao.repository_inmemory import RepositoryInMemory
from dao.student_repository import StudentRepository


class StudentRepositoryInMemory(RepositoryInMemory, StudentRepository):
    def __init__(self, id_generator: IdGenerator):
        super().__init__(id_generator)

    def find_by_fn(self, student_fn):
        for entity in self._entities.values():
            if entity.fn == student_fn:
                return entity
        return None



