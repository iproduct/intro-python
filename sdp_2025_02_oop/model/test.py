from model.question import Question


# class TestIterator:
#     def __init__(self, questions):
#         self.questions = questions
#         self.pos = -1
#     def __next__(self) -> Question:
#         if self.pos == len(self.questions) - 1:
#             raise StopIteration
#         else:
#             self.pos += 1
#             return self.questions[self.pos]


class Test:
    def __init__(self, title:str=None, questions: list[Question] = None, minutes:int=None, id: str=None):
        self.id = id
        self.title = title
        self.questions = questions if questions is not None else []
        self.minutes = minutes

    def __str__(self):
        questions_str = ''.join(map(lambda question: str(question), self.questions))
        return f'Test: {self.title}\n{questions_str}\n'

    def __iter__(self):
        return iter(self.questions)
        # return TestIterator(self.questions)



