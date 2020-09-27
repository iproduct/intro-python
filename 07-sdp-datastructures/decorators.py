from student import Student
import time

def decorator(delegate):
    def wrapper(*args, **kwargs):
        print('Before delegate')
        result = delegate(*args, **kwargs)
        print('After delegate')
        return result
    return wrapper;

def profile(unit = 'ns'):
    def inner(delegate):
        def wrapper(*args, **kwargs):
            before = time.time_ns()
            result = delegate(*args, **kwargs)
            after = time.time_ns()
            exec_time = after - before
            exec_time_unit = 'ns'
            if(unit == 'ms'):
                exec_time /= 1000000
                exec_time_unit = 'ms'
            print(f'Function \'{delegate.__name__}\' executed for: {exec_time} {exec_time_unit}')
            return result
        return wrapper
    return inner

@decorator
# @profile('ms')
def print_name(name):
    sum = 0
    for i in range(1, 100000):
        sum += i
    print(f'Name: {name}')
    return True

@decorator
@profile('ms')
def print_courses(student):
    sum = 0
    for i in range(1,1000000):
        sum += i
    print(student.courses)
    return len(student.courses)

if __name__ == '__main__':
    res = print_name('Python')
    print(res)
    num_courses = print_courses(Student('7009122345', 'Dimitar', 'Georgiev', 'Plovdiv', '+359889675432',
                     ['Algebra', 'SDP', 'Calculus', 'Internet Programming']),)
    print(num_courses)