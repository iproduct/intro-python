from dao.id_generator import IdGenerator
from dao.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self, id_generator: IdGenerator = None):
        self.id_generator = id_generator