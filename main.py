class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 0
        self.health = 100
        self.happiness = 50

    def meow(self):
        print(f"{self.name}: Meow!")

    def eat(self, food):
        if food == "fish":
            self.hunger = 0
            self.health += 10
            self.happiness += 5
            print(f"{self.name}: Yummy! I love fish!")
        else:
            self.hunger += 1
            self.health -= 5
            print(f"{self.name}: I don't like {food}.")

    def play(self):
        self.happiness += 10
        print(f"{self.name}: I'm having fun!")


def play_with_cat(cat):
    cat.play()


def feed_cat(cat, food):
    cat.eat(food)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 0

    def talk(self):
        print(f"{self.name}: Hello, I'm {self.name}. Nice to meet you!")
