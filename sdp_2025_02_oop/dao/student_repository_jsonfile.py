from dao.id_generator import IdGenerator
from dao.repository_inmemory import RepositoryInMemory
from dao.repository_jsonfile import RepositoryJsonFile
from dao.student_repository import StudentRepository
from decorators.singleton import singleton


@singleton
class StudentRepositoryJsonFile(StudentRepository, RepositoryJsonFile):

    def find_by_fn(self, student_fn):
        for entity in self._entities.values():
            if entity.fn == student_fn:
                return entity
        return None



