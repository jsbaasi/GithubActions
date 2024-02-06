import os

def CryptographicAlgorithmMD5():
    return

class Player():
    """Class representing a player."""

    def __init__(self, initialAmount = 100):
        if initialAmount == 0:
            self.health = 0
            self.alive = False
        else:
            self.health = initialAmount
            self.alive = True

    def hitPlayer(self, damageAmount):
        if self.alive == False:
            raise PlayerNotAlive("Player is not alive")
        elif damageAmount >= self.health:
            self.alive = False
        else:
            self.health -= damageAmount

    def healPlayer(self, healAmount):
        if self.alive == False:
            raise PlayerNotAlive("Player is not alive")
        elif (self.health + healAmount) >= 100:
            self.health = 100
        else:
            self.health += healAmount

class PlayerNotAlive(Exception):
    pass
