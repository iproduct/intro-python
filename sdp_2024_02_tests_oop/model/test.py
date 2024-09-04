from model.question import Question


class Test:
    def __init__(self, id: str=None, title:str=None, questions: list[Question] = None, minutes:int=None):
        self.id = id
        self.title = title
        self.questions = questions if questions is not None else []
        self.minutes = minutes

    def __str__(self):
        questions_str = ''.join(map(lambda question: str(question), self.questions))
        return f'Test: {self.title}\n{questions_str}\n'


