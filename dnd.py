from random import *
from math import *


class Player:

    def __init__(self, author, abilities = {
    'strength': 0,
    'dexterity': 0,
    'constitution': 0,
    'intelligence': 0,
    'wisdom': 0,
    'charisma': 0
    }, name = ""):
        self.user = str(author)
        self.name = name
        self.abilities = abilities
        self.money = 0
        self.items = []

    def set_name(self, name):
        self.name = name

    def update_ability(self, ability, value):
        self.abilities[ability] = value

    def add_ability(self, ability, value):
        self.abilities[ability] += value

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        try:
            self.items.remove(item)
        except:
            pass

    def add_money(self, money):
        self.money += int(money)


    def roll(self, ability, advantage = 0):
        reply = ""
        dice = 0
        if advantage == 1 or advantage == -1:
            dice1 = randint(1, 20)
            dice2 = randint(1, 20)
            if advantage == 1:
                dice = max(dice1, dice2)
                reply += "you rolled a " + str(dice1) + " and a " + str(dice2) + ". having the advantage, your dice value is " + str(dice) + "."
            else:
                dice = min(dice1, dice2)
                reply += "you rolled a " + str(dice1) + " and a " + str(dice2) + ". having the disadvantage, your dice value is " + str(dice) + "."
        else:
            dice = randint(1, 20)
            reply += "you rolled a " + str(dice) + "."


        value = dice + floor((self.abilities[ability] - 10) / 2)
        reply += "\nwith an ability of " + str(self.abilities[ability]) + ", you added a modifier of " + str(floor((self.abilities[ability] - 10) / 2)) + " to your dice score.\nthat puts your " + ability + " check at " + str(value) + "."

        return reply


def roll(count:int = 1, dice:int = 20, extra:int = 0):
    rolled = []
    value = 0
    for i in range(0, count):
        rolled.append(randint(1, dice))
        value += rolled[i]

    value += extra

    return [rolled, value]
