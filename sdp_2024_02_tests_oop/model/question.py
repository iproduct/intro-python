from model.answer import Answer
from enum import Enum

# class syntax
class QuestionType(Enum):
    MULTIPLE_CHOICE = 1
    MULTIPLE_RESPONSE = 2
    OPEN_QUESTION = 3

class Question:
    def __init__(self, question:str=None, answers:list[Answer]=None, points:int=None, type:QuestionType=QuestionType.MULTIPLE_CHOICE ):
        self.question = question
        self.answers = answers if answers is not None else []
        self.points = points
        self.type = type
