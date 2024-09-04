from model.question import Question


class Test:
    def __init__(self, title:str=None, questions: list[Question] = None, minutes:int=None):
        self.title = title
        self.questions = questions if questions is not None else []
        self.minutes = minutes

