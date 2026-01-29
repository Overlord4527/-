import time
import random
class Resident:
    def __init__(self, name):
        self.name = name
        self.hunger = 60
        self.energy = 80
        self.is_alive = True

    def status(self):
        return f"{self.name} | Голод: {self.hunger} | энергия: {self.energy}"

    def live_dey(self):
        self.hunger -= 15
        self.energy -= 15
        if self.hunger <= 0 or self.energy <= 0:
            self.is_alive = False
    def react_to_mess(self):
        pass
class WorkerSim (Resident):
    def _init_(self, name, money):
        super().__init__(name)
        self.money = money
    def work(self):
        print(f" {self.name} пашет на двух работах! +150$")
        self.money += 150
        self.energy -= 40
        self.hunger -= 20
    def react_to_mess(self):
        print(f" {self.name}: Опять этот мусор! Сил моих нет! (Минус 20 настроения)")
        self.energy -= 10
class LazySim(Resident):
    def _init__(self, name):
        super().__init__(name)
        self.laziness = 100
    def live_day(self):
        self.hunger -= 5
        self.energy -= 5
        if self.hunger <= 0 or self.energy <= 0:
            self.is_alive = False
    def sleep_on_trash (self):
        print(f" {self.name} прилег на гору грязного белья. Удобно!")
        self.energy += 40
        self.hunger -= 5
    def react_to_mess(self):
        print(f"😋 {self.name}: 'Какой мусор? Это же элементы интерьера...'")
worker = WorkerSim("Артур (работяга)", 1003)
lazy_guy = LazySim("Ларри (Ленц)")
roommantes = [worker, lazy_guy]
day = 1
is_messy = True
print("СИМУЛЯТОР КОММУНАЛКИ ЗАПУЩЕН")
while True:
    print(f"\n=== ДЕНЬ {day} ===")
    if not all(r.is_alive for r in roommantes):
        dead = next(r for r in roommantes if not r.is_alive)
        print(f"КОНЕЦ ИГРЫ: {dead.name} покинул этот мир.")
        break
    print(f"Общак Артура: {worker.money}$ | Состояние: {'Хлам' if is_messy else 'Чисто'}")
    for r in roommantes:
        print(r.status())
    print("\nВаш выбор:")
    print("1. Артур: Пойти на работу (+150)")
    print("2. Артур: Купить пиццу на всех")
    print("3. Ларри: Поспвть в куче хлама (+энегия)")
    print("4. Ларри: Попросить у Артура денег на еду")
    print("5. Убраться в комнате (Артур тратит энергию)")
    print("0. Выход")
    choice = input("Действие:")
    if choice == "1":
        worker.work()
    elif choice == "2":
        if worker.money >= 50:
            worker.money -= 50
            for r in roommantes:
                r.hunger = min(100, r.hunger + 40)
                print("Пицца заказана! Все поели.")
            else:
                print("Нет денег на пиццу!")
        elif choice == "3":
            if is_messy:
                lazy_guy.sleep_on_trash()
            else:
                print("Хлама нет, пришлось спать на голом полу. Спина болит.")
                lazy_guy.energy += 10
        elif choice == "4":
            print(f"Ларри клянчит деньги. Артур в ярости!")
            worker.energy -= 5
        elif choice == "5":
            print(f"Артур вынес 40 мешков мусора.")
            is_messy = False
            worker.energy -= 30
        elif choice == "0":
            break
        print("\n Ночь в комуналке...")
        time.sleep(1)
        for r in roommantes:
            r.live_day()
            if is_messy:
                r.react_to_mess()
        day += 1
print("Игра завершена.")