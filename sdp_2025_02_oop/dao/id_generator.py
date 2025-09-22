from abc import ABC, abstractmethod


class IdGenerator(ABC):
    @abstractmethod
    def generate_id(self):
        """
        Generate a unique ID
        :return: the generated ID
        """
        pass