# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return f"{self.name} издает какой-то звук"
# my_cat = Cat("Мурчит")
# print(my_cat.speak())
# my_cat.name = "Барсик"
# print(my_cat.name)

# class Zombie:
#     pass
# zombie1 = Zombie()
# zombie2 = Zombie()
# print(zombie1)
# print(zombie2)
# print(type(zombie1))

# class Zombie:
#     def __init__(self,name):
#         self.name = name
#         self.health = 50
# z1 = Zombie('Кровавый')
# print(z1.name)
# print(z1.health)

# class Zombie:
#     def __init__(self,name):
#         self.name = name
#         self.health = 50
#     def grow(self):
#         return F"{self.name}: УУУУ!"
# z1 = Zombie("Кровавый")
# print(z1.grow())

print("👾=== БИТВА ГЕРОЕВ ===\n")
# КЛАСС 1: ЧЕРТЕЖ ГЕРОЯ
class Character:
    def __init__(self, name, health=100, max_health=None, damage=20):
        self.name = name
        self.health = health
        self.max_health = max_health or health
        self.damage = damage
    def staus(self):
        percent = (self.health / self.max_health) * 100
        return f"🔪{self.name}: {self.health}/{self.max_health} HP ({percent:.0f}%)| урон: {self.damage}"
    def attack(self, tager):
        return f"🔪 {self.name} бьет {tager.name} на {self.damage}"
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return f"💥 {self.name} получил {damage} урона! Осталось: {self.health} HP"
    def is_alive(self):
        return self.health > 0
class Enemy:
    def __init__(self, name, health=60, damage=15):
        self.name = name
        self.health = health
        self.damage = damage
        self.max_health = health
    def staus(self):
        percent = (self.health / self.max_health) * 100
        return f"🧟‍{self.name}: {self.health}/{self.max_health} HP ({percent:.0f}%)| урон: {self.damage}"
    def attack(self, tager):
        return f"⚔ {self.name} бьет {tager.name} на {self.damage}!"
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return f"☠ {self.name} получил {damage} урона! Осталось: {self.health} HP"
    def is_alive(self):
        return self.health > 0
print("🏭 СОБИРАЕМ АРМИЮ ПО ЧЕРТЕЖАМ...\n")
hero = Character("🛡 Артур", 120, damage=25)
goblin = Enemy("👺 Гоблин", 50, 12)
boss = Enemy("🐲 Дракон", 200, 30)
army = [hero, goblin, boss]
print("СОСТАВ АРМИИ")
for unit in army:
    print(unit.staus())
print("\n" + "=" * 50 + "\n")
def battle_round(attacher, defender):
    """Один раунд боя"""
    print(f"\n🔥 РАУНД БОЯ:")
    print(attacher.staus())
    print(defender.staus())
    print(attacher.attack(defender))
    print(defender.take_damage(attacher.damage))
    print(defender.staus())
    print("-" * 30)
print("⚔ НАЧИНАЕТСЯ БИТВА!\n")
battle_round(goblin, hero)
battle_round(hero, goblin)
battle_round(boss, hero)
battle_round(hero, boss)
print("\n" + "=" *50 + "\n")
print("ИТОГ БОЯ:")
for unit in army:
    status = unit.staus()
    if not unit.is_alive():
        status += "МЕРТВ"
    print(status)
print("\n === КОНЕЦ ДЕМОНСТРАЦИИ ООП ===\n")
print("КЛССЫ = ЧЕРТЕЖИ ")
print("ОБЬЕКТЫ = ФИГУРКИ")
print("МЕТОДЫ = УМЕНИЯ")
print("Атрибуты = характеристики (урон, здоровье)")
print("Готово к уроку - тестировано!"),
