
# with super
class A(object):
    def __new__(cls):
        print('creating instance with new')
        return super(A, cls).__new__(cls)

    def __init__(self):
        print('init was called after')

a1 = A()

# without super

class B(object):
    def __new__(cls):
        print('creating instance with new')

    def __init__(self):
        print('init was called')

a1 = B()
