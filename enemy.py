import random


class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self,name):
        super().__init__(name,health=100,attackPower=7)

    def attack(self):
        """Return a random amount of damage."""
        return random.randint(1, self.attack_power)
    def stealGold(self,hero):
        """GOBBOS TAKIN HEROS GOLD"""
        self.gold= self.gold+ hero.gold
        hero.gold=0
        print("GET REKT NOOB")
    