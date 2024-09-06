from model.answer import Answer
from model.question import Question, QuestionType
from view.view import View

class QuestionView(View):
    def inputQuestion(self) -> Question:
        q = Question()
        while True:
            q.text = input('Question text:').strip()
            if len(q.text) >0:
                break
            print('Question text is required')
        while True:
            try:
                choice = int(input(f'Question type: {[f"{t[0] + 1}). {t[1].name}" for t in enumerate(QuestionType)]}:'))
                if choice < 1 or choice > len(QuestionType):
                    raise ValueError
                q.type = [t for t in QuestionType][choice-1]
                break
            except (ValueError, IndexError):
                print('Invalid choice. Try again')
        while True:
            answer = input('Next answer [<Enter> for end]:')
            if len(answer) == 0:
                break
            while True:
                try:
                    points = int(input('Answer points (integer or <Enter> for 0):'))
                    break
                except ValueError:
                    print('Points should be an integer number')
            q.answers.append(Answer(answer, points))
        return q
