from model.answer import Answer
from enum import Enum

# class syntax
class QuestionType(Enum):
    MULTIPLE_CHOICE = 1
    MULTIPLE_RESPONSE = 2
    OPEN_QUESTION = 3

class Question:
    def __init__(self, text:str=None, answers:list[Answer]=None, weight:float=1, type:QuestionType=QuestionType.MULTIPLE_CHOICE):
        self.text = text
        self.answers = answers if answers is not None else []
        self.weigth = weight
        self.type = type

    def __str__(self):
        answers_str = '   - ' + '\n   - '.join(map(lambda answer: str(answer), self.answers))
        return f'Q: {self.text} [{str(self.type).split('.')[1]}] - W: {self.weigth}\n{answers_str}\n'

    def __iter__(self):
        return iter(self.answers)
