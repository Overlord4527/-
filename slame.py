# class Sim:
#     def __init__(self, name, energy=50):
#         self.name = name
#         self.energy = energy
# class Bed:
#     def use_for_sleep(self, sim):
#         sim.energy = 100
# my_sim = Sim(name ="Bob")
# my_bed = Bed()
# my_bed.use_for_sleep(my_sim)
# print(F"Энергия Сима {my_sim.name} теперь {my_sim.energy}")

class Home:
    def __init__(self, name):
        self.name = name
    def sleep(self, sim):
        print(f"{sim.name} спит в доме {self.name}")
        sim.energy += 20
    def relax(self, sim):
        sim.energy += 10
        print('Storm Spirit is relaxing: +10 energy')
class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary
    def work(self, sim):
        print("f{sim.name} работает как {self.title} ")
        sim.money += self.salary
        sim.energy -= 15

class Sim:
    def __init__(self, name, home, job):
        self.name = name
        self.energy = 50
        self.money = 100
        self.home = home
        self.job = job
    def eat(self):
        print(f"{self.name} ест 🧀")
        self.energy+=10
        self.money-=5
    def snof_status(self):
        print("------")
        print(f"Имя: {self.name}")
        print(f"Энергия: {self.energy}")
        print(f"Деньги: {self.money}")

        if self.energy <= 0:
            print('Sim is tired')
        if self.money <=0:
            print('Sim without money')

class Haymer:
    def __init__(self, title2, salary2):
        self.title2 = title2
        self.salary2 = salary2

    def work2(self, sim):
        print(f'{sim.name} is working  {self.title2}, он получает 30 dollars and -5 энергии')
        sim.money += self.salary2
        sim.energy -= 5
home= Home("Уютный дом")
job = Job("Програмист", 50)
sim = Sim("Алекс", home, job)
sim.snof_status()
sim.job.work(sim)
sim.home.sleep(sim)
sim.eat()
home.relax(sim)
work2 = Haymer(title2='геймер', salary2=30)
work2.work2(sim)
sim.snof_status()
