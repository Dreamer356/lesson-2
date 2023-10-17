import random

class Student:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money
        self.energy = 100
        self.knowledge = 0

    def work(self):
        if self.energy >= 20:
            earnings = random.randint(10, 30)
            self.money += earnings
            self.energy -= 20
            print(f"{self.name} worked and earned ${earnings}.")
        else:
            print(f"{self.name} is too tired to work.")

    def study(self):
        if self.money >= 10:
            knowledge_gained = random.randint(5, 15)
            self.knowledge += knowledge_gained
            self.money -= 10
            print(f"{self.name} studied and gained {knowledge_gained} knowledge points.")
        else:
            print(f"{self.name} doesn't have enough money to study.")

    def rest(self):
        if self.money >= 5:
            self.energy = 100
            self.money -= 5
            print(f"{self.name} took a rest and regained energy.")
        else:
            print(f"{self.name} doesn't have enough money to rest.")

    def live_one_year(self):
        for _ in range(365):
            action = random.choice([self.work, self.study, self.rest])
            action()

    def status(self):
        print(f"{self.name}: Money = ${self.money}, Energy = {self.energy}, Knowledge = {self.knowledge}")

if __name__ == "__main__":
    student = Student("Vlad", money=50)

    for _ in range(3):
        student.live_one_year()
        student.status()
        print("-" * 20)