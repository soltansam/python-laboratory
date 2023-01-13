from eckel import Simple


class Simple2(Simple):
    def __init__(self, str):
        print('print statement inside simple2 class constructor')
        # you must call the base-class constructor
        Simple.__init__(self, str)
    def display(self):
        self.showMsg('called from display()')
    # overriding the base class method
    def show(self):
        print('overridden show() method')
        # calling a base-class method from inside
        # the overridden mehtod:
        Simple.show(self)

class Different:
    def show(self):
        print('not derived from simple')

if __name__ == "__main__":
    x = Simple2('Simple2 constructor argument')
    x.display()
    x.show()
    x.showMsg('inside main')
    def f(obj): obj.show() # one line definition
    f(x)
    f(Different())
