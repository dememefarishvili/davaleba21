class Cat:
    def eat(self):
        print("Cat eats a milk")

    def talk(self):
        print("Cat says miaww")

    def walk(self):
        print("Cat can run 20km/h")


class Dog:
    def eat(self):
        print("Dog eats a bone")

    def talk(self):
        print("Dog says Aww")

    def walk(self):
        print("Dog can run 40km/h")



cat = Cat()
dog = Dog()

animals = (cat, dog)

for animal in animals:
    animal.eat()
    animal.talk()
    animal.walk()