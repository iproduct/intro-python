import re

from controller.test_controller import TestController
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
    test = Test('9c5b94b1-35ad-49bb-b118-8e8fc24abf80', 'Python OOP', questions, minutes=10)
    print(test)
    # for question in test:
    #     print(question.text)
    #
    #     # print answers and compute max_points
    #     i = 1
    #     max_points = 0
    #     for answer in question:
    #         print(f'{i}). {answer.text}')
    #         max_points += answer.points if answer.points > 0 else 0
    #         i += 1
    #
    #     # input and evaluate student answer
    #     if question.type == QuestionType.MULTIPLE_CHOICE:
    #         choice = int(input('Select answer:'))
    #         result = question.answers[choice - 1].points
    #         if result > 0:
    #             print(f'Correct answer - {result} points')
    #         else:
    #             print(f'Incorrect answer - {result} points')
    #     elif question.type == QuestionType.MULTIPLE_RESPONSE:
    #         choices_str = input('Select one or more answers separated with comma:')
    #         choices = map(lambda s: int(s), re.split('\\W+',choices_str))
    #         result = 0
    #         for choice in choices:
    #             result += question.answers[choice - 1].points
    #         if result == max_points:
    #             print(f'Correct answer - {result} points')
    #         elif result > 0:
    #             print(f'Partially correct answer - {result} points')
    #         else:
    #             print(f'Incorrect answer - {answer[choice - 1]} points')
    #     print()

    controller = TestController()
    # controller.current_test = test
    # controller.saveTest()
    controller.loadTest('9c5b94b1-35ad-49bb-b118-8e8fc24abf80')
    print('\nAFTER JSON DESERIALIZATION:')
    print(controller.current_test)