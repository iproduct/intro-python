class Sample:
  x = 42  # class attribute

  @staticmethod
  def increment_static():
    __class__.x += 1

  @classmethod
  def increment_class(cls):
    cls.x += 1

  def __init__(self, num):
    self.age = num

  def get_x(self):
    self.__class__.x

  def increment_x(self):
    self.__class__.x +=  1

if __name__ == '__main__':
  s1 = Sample(25)
  Sample.increment_static()
  Sample.increment_class()
  print(Sample.x)
  print(s1.age)