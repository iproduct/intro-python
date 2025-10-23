from abc import ABC, abstractmethod


#IdGenerator interface
class IdGenerator(ABC):
    @abstractmethod
    def get_next_id(self) -> str: pass