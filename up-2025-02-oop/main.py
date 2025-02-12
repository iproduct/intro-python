from model.instructor import Instructor
from model.student import Student

if __name__ == '__main__':
    trayan = Instructor('Trayan Iliev', 'Sofia 1000', '0887453214', 'trayan@gmail.com',
                        '', '305', courses= ['UP', 'SDP', 'IA with Gen AI'])
    print(trayan)

    george = Student('George', fn='0PH23235', semester=1)
    print(george)

