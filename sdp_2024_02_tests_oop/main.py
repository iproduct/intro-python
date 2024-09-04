from model.test import Test
from model.question import Question, QuestionType
from model.answer import Answer

if __name__ == '__main__':
    questions = [
        Question('Does Python support multiple inheritsance?',
                 [
                     Answer('Yes', 1 ),
                     Answer('No', 0 ),
                 ], 3),
        Question('Which types are immutable in Python?',
                 [
                     Answer('str', 1 ),
                     Answer('int', 1 ),
                     Answer('list', 0 ),
                     Answer('dict', 0 ),
                     Answer('set', 0 ),
                     Answer('tuple', 1 ),
                 ], 1, QuestionType.MULTIPLE_RESPONSE),
    ]
    test = Test('1', 'Python OOP', questions)
    print(test)