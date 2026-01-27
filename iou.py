import time
import random
class Sim:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 100
        self.is_alive = True
    def eat(self):
        if self.hunger >= 100:
            print(f"{self.name} не хочет есть.")
        else:
            self.hunger += 20
            self.energy -= 5
            print(f"{self.name} поел(а). Голод: {self.hunger}")
    def live_dey(self):
        self.hunger -= 10
        self.energy -= 10
        if self.hunger <= 0 or self.energy <= 0:
            self.is_alive = False
            print(f"{self.name} не выжержал суровой жизни и покинул чат.")
    def status(self):
        return f"{self.name} | Голод: {self.hunger} | энергия: {self.energy}"
################################################################################################################
class Human(Sim):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job
        self.money = 50
    def work(self):
        self.energy -= 30
        self.hunger -= 20
        self.money += 100
        print(f"{self.name} сходил на работу ({self.job}). +100$. Энергия: {self.energy}")
    def feed_pet(self, pet):
        if self.money >= 20:
            print(f"{self.name} покупает корм и кормит {pet.name}...")
            self.money -= 20
            pet.eat()
        else:
            print(f" у  {self.name} нет денег на корм! Иди работай!")
    def feed_zombie(self, pet):
        if self.money >= 25:
            print(f"{self.name} покупает корм и кормит {zombie.name}...")
            self.money -= 25
            zombie.eat()
        else:
            print(f" у  {self.name} нет денег на еду! беги!!!!")
    def feed_pet_fish(self, pet_fish):
        if self.money >= 20:
            print(f"{self.name} покупает корм и кормит {pet_fish.name}...")
            self.money -= 20
            pet_fish.eat()
        else:
            print(f" у  {self.name} нет денег на корм для рыбок! Иди работай!")
    def repair_robot(self, robot):
        print(f"{self.name} чинит {robot.name}...")
        self.energy -= 20
        robot.energy = 100
        print(f"{robot.name} полностью заряжен!")
##################################################################################################################
class Dog(Sim):
    def eat(self):
        self.hunger += 30
        print(f"🐶{self.name} жадно грызет кость! Гав!")
    def play(self,human):
        print(f"{self.name} приносит мячик {human.name}.")
        self.energy -= 20
        human.energy += 10
        print(f'{human.name} повеселел!')
###############################################################################################################
class Cat(Sim):
    def __init__(self, name):
        super().__init__(name)
        self.lives = 9

    def eat(self):
        self.hunger += 30
        print(f"🐈{self.name}: Мяу! Рыбка! ")
    def play(self,human):
        print(f"{self.name} играет с {human.name}.")
        self.energy -= 20
        human.energy += 10
        print(f'{human.name} повеселел!')
    def tear_sofa(self):
        self.energy -= 10
        print(f'🐈 {self.name} подрал диван, человек будет в ярости')

###############################################################################################################
class pet_fish(Sim):
    def eat(self):
        self.hunger += 20
        print(f"🐠 {self.name} ест плавующий корм")

    def play(self, human):
        print(f"{self.name} радует своей красатой {human.name}.")
        self.energy -= 15
        human.energy += 5
        print(f"{human.name} повеселел")
##################################################################################################################
class Robot(Sim):
    def __init__(self, name):
        super().__init__(name)
        self.battery = 100
    def life_day(self):
        self.energy -= 5
    def eat(self):
        print(f"{self.name} подключается к розетке. Зарядка...")
        self.energy = 100
    def cook_dinner(self,human):
        if self.energy > 20:
            print(f"{self.name} готовит ужин для {human.name}")
            self.energy -= 20
            human.eat()
        else:
            print(f"{self.name} : БАТАРЕЯ РАЗРЯЖЕНА. НЕ МОГУ ГОТОВИТЬ.")
#############################################################################################################
class Zombie(Sim):
    def eat(self):
        self.hunger += 30
        print(f"{self.name} жадно ест еду")
    def life_day(self):
        self.hunger -= 10
    def looking_for_food(self,human):
        if self.energy > 20:
            print(f"🧟‍{self.name} не обращяет внимания на {human.name}")
        else:
            print(f"🧟‍{self.name} атакует {human.name}")
            human.energy -= 1000
            zombie.hunger += 80
#################################################################################################################
class robot_vacuum_cleaner(Sim):
    def __init__(self, name):
        super().__init__(name)
        self.battery = 100
    def life_day(self):
        self.energy -= 5
    def eat(self):
        print(f"{self.name} подключается к розетке. Зарядка...")
        self.energy = 100
    def cleans_the_house(self,human):
        if self.energy > 20:
            print(f"{self.name} уберает дом  для {human.name}")
            self.energy -= 20
            human.energy += 5
            print(f"{human.name} повеселел")
        else:
            print(f"{self.name} : БАТАРЕЯ РАЗРЯЖЕНА. НЕ МОГУ Убирать.")
###############################################################################################################
player = Human("Алекс", "Програмист")
doggo = Dog("Бобик")
pet_fish = pet_fish("Аркадий")
robo = Robot("робо_дима")
robot_vacuum_cleaner = robot_vacuum_cleaner("Элеонора Андреевна")
barsik = Cat("барсик")
zombie = Zombie("Дэйв")
household = [player, doggo, pet_fish, robo, robot_vacuum_cleaner, barsik, zombie]
day = 1
print("ДОБРО ПОЖАЛОВАТЬ В SIMS: PYTHON EDITION")
while True:
    print(f"\n ДЕНЬ {day} ===")
    game_over =False
    for sim in household:
        if not sim.is_alive:
            print(f"GAME OVER: {sim.name} погиб")
            game_over = True
    if game_over:
        break
    print(f"Деньги: {player.money}$")
    for sim in household:
        print(sim.status())
    print("\n Что будет делать алекс?")
    print("1. Пойти на работу")
    print("2. Поесть самому (-20$ еда)")
    print("3. Покормить Бобика (-20$ корм)")
    print("4. Поиграть с Бобиком")
    print("5. Попросить робота приготовить ужин (Бесплатно)")
    print("6. Починить робота")
    print("7. Покормить Аркадия (-20$ корм)")
    print("8. Поиграть с Аркадием")
    print("9. Попросить Элеонору Андреевну убрать дом (Бесплатно)")
    print("10. Починить Элеонору Андреевну")
    print("11. Покормить Барсика (-20$ корм)")
    print("12. Поиграть с Барсиком")
    print("13.Барсик подрет диван")
    print("14 покормить зомби")
    print("0. Выход")
    choice = input("Твой выбор")
    if choice == "1":
        player.work()
    elif choice == "2":
        if player.money >= 20:
            player.money -= 20
            player.eat()
        else:
            print("Нет денег!")
    elif choice == "3":
        player.feed_pet(doggo)
    elif choice == "4":
        doggo.play(player)
    elif choice == "5":
        robo.cook_dinner(player)
    elif choice == "6":
        player.repair_robot(robo)
    elif choice == "7":
        player.feed_pet(pet_fish)
    elif choice == "8":
        pet_fish.play(player)
    elif choice == "9":
        robot_vacuum_cleaner.cleans_the_house(player)
    elif choice == "10":
        player.repair_robot(robot_vacuum_cleaner)
    elif choice == "11":
        player.feed_pet(barsik)
    elif choice == "12":
        barsik.play(player)
    elif choice == "13":
        barsik.tear_sofa()
    elif choice == "14":
        player.feed_zombie(zombie)
    elif choice == "0":
        print("Пока!")
        break
    else:
        print("Неверная команда, день прошел впустую...")
    print("\n Наступает ночь... Все показатели падают.")
    time.sleep(1)
    for sim in household:
        sim.live_dey()
    day += 1