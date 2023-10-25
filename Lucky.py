#!/usr/bin/python3
import random
import time
class Warrior:
    players = 0
    def __init__(self, name="Player "):
        self.name = name
        self._health = 20
    def attack(self, enemy):
        damage = random.randint(0, 10)
        print(f"==>{self.name} ATTACKS {enemy.name} AND DEALS {damage} DAMAGE\n")
        enemy.health -= damage
        if enemy.health < 1:
            time.sleep(2)
            print(f"{enemy.name} has Died and {self.name} is Victorious\n\nGAME OVER\n")
            return False
        else:
            return True
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, value):
        self._health = value
        time.sleep(2)
        print(f"{self.name} IS DOWN TO {self._health} HEALTH\n")
    @health.deleter
    def health(self):
        del self


def main():
    print(99 * "#", "\n")
    print("** Usage:\n\t=> Every player picks a number, and the game will generate a random number from 0 to 20.")
    print("\t=> The closest player to the generated number will attack first.")
    print("\t=> Every player has 20 points of health and each attack is also randomized.")
    print("\t=> If both players picked the same number the game will randomly choose the first attacker.\n")
    print(99 * "#", "\n")
    try:
        player1 = input("Player 1 name: ")
        player2 = input("Player 2 name: ")
        player1_luck = int(input(f"{player1} pick your number: "))
        player2_luck = int(input(f"{player2} pick your number: "))
    except (ValueError, TypeError):
        print("Quit for wrong input, not number.")
        exit(99)
    except (EOFError, UnboundLocalError, KeyboardInterrupt):
        print("\nGoodbye!!")
        exit(0)
    lucky = random.randint(1, 20)
    if player1_luck == player2_luck:
        print("Same number, 100% luck now.")
        time.sleep(1.5)
        while player1_luck == player2_luck:
            player1_luck = random.randint(1, 20)
            player2_luck = random.randint(1, 20)
    print("Generating Luck...")
    time.sleep(2)
    print(f"Player 1 number is: {player1_luck}")
    time.sleep(1.5)
    print(f"Player 2 number is: {player2_luck}")
    time.sleep(1.5)
    print(f"LUCKY NUMBER IS: {lucky}")
    time.sleep(3)
    player1 = Warrior(player1)
    player2 = Warrior(player2)
    if abs(player1_luck - lucky) <= abs(player2_luck - lucky):
        print(f"{player1.name} WILL START.\n")
        time.sleep(3)
        while player1.attack(player2) and time.sleep(2) is None and player2.attack(player1):
            time.sleep(2)
    else:
        print(f"{player2.name} WILL START.\n")
        time.sleep(3)
        while player2.attack(player1) and time.sleep(2) is None and player1.attack(player2):
            time.sleep(2)
main()