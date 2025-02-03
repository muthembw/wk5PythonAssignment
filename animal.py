class Animal:
    def move(self):
        pass


class Dog(Animal):
    def move(self):
        print("The dog runs on four legs! 🐕")


class Cat(Animal):
    def move(self):
        print("The cat walks gracefully! 🐈")


class Fish(Animal):
    def move(self):
        print("The fish swims in the water! 🐟")


# Create instances and call their move method
animals = [Dog(), Cat(), Fish()]

for animal in animals:
    animal.move()
