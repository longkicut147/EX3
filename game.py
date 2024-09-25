import random

class Character:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0

class Hero(Character):
    def special_attack(self, target):
        pass

class Warrior(Hero):
    def special_attack(self, target):
        damage = self.attack_power * 2
        print(f"{self.name} performs a special attack on {target.name} for {damage} damage!")
        target.take_damage(damage)

class Mage(Hero):
    def special_attack(self, target):
        damage = self.attack_power
        print(f"{self.name} casts a powerful spell on {target.name} for {damage} damage!")
        target.take_damage(damage)

class Monster(Character):
    def roar(self):
        pass

class Orc(Monster):
    def roar(self):
        print(f"The Orc lets out a terrifying roar! {self.name} is ready to fight!")

class Dragon(Monster):
    def roar(self):
        print(f"The Dragon breathes fire as it roars! {self.name} is preparing to attack!")

def battle(hero, monster):
    print(f"--- Battle Start: {hero.name} vs {monster.name} ---")
    
    monster.roar()

    while hero.is_alive() and monster.is_alive():
        if random.choice([True, False]):
            hero.attack(monster)
        else:
            hero.special_attack(monster)

        if not monster.is_alive():
            print(f"{monster.name} has been defeated!")
            break

        # Monster's turn
        monster.attack(hero)
        if not hero.is_alive():
            print(f"{hero.name} has been defeated!")
            break

    print(f"--- Battle End: {hero.name} vs {monster.name} ---")

# Create a warrior hero and a dragon monster
hero_warrior = Warrior(name="Conan", health=100, attack_power=20, defense=5)
monster_dragon = Dragon(name="Smaug", health=120, attack_power=25, defense=10)

# Start the battle
battle(hero_warrior, monster_dragon)
