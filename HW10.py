"""
Georgia Institute of Technology - CS1301
Homework 10 - Object Oriented Programming
Matthew Kistner
"""

class Pokemon:
    def __init__(self, name, lvl, typ, bag, health=50.0, alive=True):
        self.name = name
        self.level = lvl
        self.type = typ
        self.bag = bag
        self.health = health
        self.isAlive = alive
    def loseHealth(self, number):
        if self.isAlive == True:
            self.health -= 5*number
            if self.health <= 0:
                self.isAlive = False
    def gainHealth(self):
        if self.isAlive == False:
            print('{} has fainted! Cannot gain health!'.format(self.name))
        elif self.bag.healthPotion == 0:
            print('Sorry, {} has no health potions!'.format(self.name))
        else:
            if self.health <= 30.0:
                self.health += 20.0
                self.bag.healthPotion -= 1
            else:
                self.health = 50.0
                self.bag.healthPotion -= 1
    def surrender(self):
        self.bag.whiteFlag = True
    def __eq__(self, other):
        return self.name == other.name and self.type == other.type
    def __str__(self):
        return "This is {} type Pokemon {} with level {}, current health is {}.".format(self.type, self.name, self.level, self.health)
pass
        
        
#########################################################


class Bag:
    def __init__(self, hP, flag=False):
        self.healthPotion = hP
        self.whiteFlag = flag
    #provided
    def __eq__(self, other):
        return self.healthPotion == other.healthPotion and self.whiteFlag == other.whiteFlag
pass
    
#########################################################


class Lobby:
    def __init__(self, roomName, pokeA, pokeB):
        self.roomName = roomName
        self.pokeA = pokeA
        self.pokeB = pokeB
    def battle(self):
        self.pokeA.whiteFlag = False
        self.pokeB.whiteFlag = False
        if self.pokeA.type == self.pokeB.type:
            self.pokeA.loseHealth(1)
            self.pokeB.loseHealth(1)
        elif (self.pokeA.type == 'Fire' and self.pokeB.type == ' Water') or (self.pokeA.type == 'Water' and self.pokeB.type == 'Grass') or (self.pokeA.type == 'Grass' and self.pokeB.type == 'Fire'):
            self.pokeA.loseHealth(2)
            self.pokeB.loseHealth(0.5)
        elif (self.pokeB.type == 'Fire' and self.pokeA.type == ' Water') or (self.pokeB.type == 'Water' and self.pokeA.type == 'Grass') or (self.pokeB.type == 'Grass' and self.pokeA.type == 'Fire'):
            self.pokeA.loseHealth(0.5)
            self.pokeB.loseHealth(2)
        self.gameOver()
    def gameOver(self):
        if (self.pokeA.isAlive == False and self.pokeB.isAlive == False) or (self.pokeA.bag.whiteFlag == True and self.pokeB.bag.whiteFlag == True):
            print("It's a tie!")
            self.pokeA.whiteFlag = False
            self.pokeB.whiteFlag = False
        elif (self.pokeA.isAlive == False or self.pokeA.bag.whiteFlag == True) and self.pokeB.isAlive == True:
            print('{} won the battle'.format(self.pokeB.name))
            self.pokeB.level += 1
            self.pokeA.bag.whiteFlag = False
        elif (self.pokeB.isAlive == False or self.pokeB.bag.whiteFlag == True) and self.pokeA.isAlive == True:
            print('{} won the battle'.format(self.pokeA.name))
            self.pokeA.level += 1
            self.pokeB.bag.whiteFlag = False
    def __eq__(self, other):
        return self.roomName == other.roomName 
pass
