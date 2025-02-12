from abc import abstractmethod

from dao.repository import Repository
from model.student import Student


class StudentRepository(Repository):
    @abstractmethod
    def find_by_fn(self, student_fn):
        """
        Find student by fn
        :param student_fn: Faculty number of student
        :return: the student found
        """
        pass





