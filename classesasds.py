class Lion:

    def eat(self):
        print('lion eats its hunted animals')

    def move(self):
        print('lion moves relatively fast')


class Dier():

    def eat(self):
        print('dier eats its hunted animals')

    def move(self):
        print('dier moves relatively fast')


lion01 = Lion()
dier01 = Dier()
for animal in (lion01, dier01):
    animal.eat()
    animal.move()
