import random

class worker:
    def __init__(self, name):
        self.name = name
        self.happy = 50
        self.money = 50
        self.study_iq = 87
    def a_study(self):
        print(f"{self.name} is studing!")
        self.study_iq += 0.025
        self.money -= 0.69
        self.happy -= 0.03
    def a_chilling_out(self):
        print(f"{self.name} is chilling_out!")
        self.study_iq -= 0.005
        self.money -= 1.06
        self.happy += 0.05
    def working(self):
        print(f"{self.name} is working!")
        self.study_iq += 0.01
        self.money += 1.6
        self.happy -= 0.04
    def a_mood(self):
        if (((self.happy < 30 and self.happy > 20) and (self.money < 30 and self.money > 20))
        or ((self.happy < 30 and self.happy > 20) or (self.money < 30 and self.money > 20))):
            print("Not bad")
        elif (((self.happy < 20 and self.happy > 10) and (self.money < 20 and self.money > 10))
        or ((self.happy < 20 and self.happy > 10) or (self.money < 20 and self.money > 10))):
            print("Bad")
        elif ((self.happy < 10 and self.money < 10) or (self.happy < 10 or self.money < 10)):
            print("Very bad")
        elif (((self.happy >= 50 and self.happy < 60) and (self.money >= 50 and self.money < 60))
        or ((self.happy >= 50 and self.happy < 60) or (self.money >= 50 and self.money < 60))):
            print("Good")
        elif ((self.happy <= 60 and self.money <= 60) or (self.happy <= 60 or self.money <= 60)):
            print("Very good!")
    def information(self):
        print(f"Person: {self.name}")
        print(f"Mood: {self.happy}")
        print(f"Money: {self.money}")
        print(f"IQ: {self.study_iq}")
        print("----------------------------------------")
    def a_day(self):
        random_day = random.randint(1,3)
        if random_day == 1:
            self.a_study()
            self.a_mood()
            self.information()
        elif random_day == 2:
            self.working()
            self.a_mood()
            self.information()
        elif random_day == 3:
            self.a_chilling_out()
            self.a_mood()
            self.information()

person1 = worker(name = "Oleksiy")

for day in range(365):
    print(f"Day№ {day}")
    person1.a_day()