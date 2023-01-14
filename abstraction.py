from abc import ABC
from abc import abstractmethod

class MyAbstract(ABC):

    @abstractmethod
    def my_abs_fun(self):
        print('i am surprised an abstract class is instantiated!')


m1 = MyAbstract()
m1.my_abs_fun()
