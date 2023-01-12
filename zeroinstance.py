# class Test:
#     pass


# c1 = Test()
# c2 = Test()
# print(c1)
# print(c2)
# <__main__.Test object at 0x7fe0293533d0>
# <__main__.Test object at 0x7fe029353a00>


class meta_zero_instance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('instantiation blocked by meta class!')


class Test2(metaclass=meta_zero_instance):
    pass

# c1 = Test2()
