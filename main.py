import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.hunger = 100
        self.reputation = 0
        self.alive = True

    def to_study(self):
        print("Время учебы")
        self.progress += 0.12
        self.gladness -= 5
        self.money += 5
        self.hunger -= 10
        self.reputation += 0.5

    def to_sleep(self):
        print("Время сна")
        self.gladness += 3
        self.money -= 2
        self.hunger -= 3
        self.reputation -= 0.3

    def to_chill(self):
        print("Время отдыха")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 5
        self.reputation -= 0.5

    def to_work(self):
        print("Время работы")
        self.gladness -= 7
        self.progress += 0.1
        self.money += 20
        self.hunger -=4

    def to_podrabotka(self):
        print("Заработал")
        self.gladness -= 3
        self.progress += 0.03
        self.money += 10
        self.hunger -= 1.6

    def to_kafe(self):
        print("Поел")
        self.gladness += 4
        self.progress -= 0.08
        self.money -= 10
        self.hunger += 20

    def podarok_uchitelu(self):
        print("Подарил подарок")
        self.gladness += 5
        self.progress += 1
        self.money -= 30
        self.reputation += 1




    def is_alive(self):
        if self.progress < -0.5:
            print("================Отчисление================")
            self.alive = False
        elif self.gladness <= 0:
            print("================Смерть из-зи депресси================")
            self.alive = False
        elif self.progress > 7:
            print("================Сдал экстрен================")
            self.alive = False
        elif self.money <= 0:
            print("================Бомж================")
            self.alive = False
        elif self.hunger <= 0:
            print("================Голодная смерть================")
            self.alive = False
        elif self.hunger >= 250:
            print("================Переел================")
            self.alive = False
        elif self.reputation >=10:
            print("================Подмазали================")
            self.alive = False
        elif self.reputation <= -4:
            print("================Выгнали================")
            self.alive = False

    def end_of_day(self):
        print(f"Счастье = {self.gladness}")
        print(f"Прогресс учебы = {round(self.progress, 2)}")
        print(f"Репутация = {self.reputation}")
        print(f"Голод = {self.hunger}")
        print(f"Деньги = {self.money}")


    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")

        live_cube = random.randint(1, 7)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        elif live_cube == 5:
            self.to_kafe()
        elif live_cube == 6:
            self.to_podrabotka()
        elif live_cube == 7:
            self.podarok_uchitelu()

        self.end_of_day()
        self.is_alive()

nick = Student(name = "Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day+1)