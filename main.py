class Student:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
        self.energy = 100
        self.knowledge = 0
    
    def study(self, hours):
        if self.energy >= hours * 10:
            self.knowledge += hours
            self.energy -= hours * 10
            print(f"{self.name} вивчив {hours} годин. Знань: {self.knowledge}, Енергія: {self.energy}")
        else:
            print(f"{self.name} занадто виснажений для вивчання")
    
    def rest(self, hours):
        self.energy += hours * 10
        if self.energy > 100:
            self.energy = 100
        self.money -= hours * 10
        if self.money < 0:
            self.go_to_work()
        print(f"{self.name} відпочив {hours} годин. Енергія: {self.energy}, Гроші: {self.money}")
    
    def go_to_work(self):
        self.money += 50
        print(f"{self.name} пішов на роботу та заробив 50 гривень. Гроші: {self.money}")
    
    def solve_problem(self):
        if self.knowledge >= 10:
            self.knowledge -= 10
            self.energy -= 10
            print(f"{self.name} вирішив проблему. Знань: {self.knowledge}, Енергія: {self.energy}")
        else:
            print(f"{self.name} не має достатньо знань для вирішення проблеми")
    
    def live(self):
        for i in range(365):
            action = random.choice(["study", "rest", "solve_problem"])
            if action == "study":
                self.study(random.randint(1, 4))
            elif action == "rest":
                self.rest(random.randint(1, 4))
            else:
                self.solve_problem()
    
        print(f"{self.name} закінчив рік. Знань: {self.knowledge}, Енергія: {self.energy}, Гроші: {self.money}")
