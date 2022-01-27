class A(object):
	def __init__(self):
		super(A, self).__init__()
		print("A")
class B(object):
	def __init__(self):
		super(B, self).__init__()
		print("B")
class C(A,B):
	def __init__(self):
		super(C, self).__init__()
		print("C")

if __name__ == '__main__':
    print(C())
    print(C.mro())