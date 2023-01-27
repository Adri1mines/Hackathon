import random
from math import *
class Ennemy:
    def __init__(self, hp, atk, position):
        self.hp = hp
        self.atk = atk
        self.position = position

    def search_player(self, player):
        player_x = player.position[0]
        player_y = player.position[1]
        x = self.position[0]
        y = self.position[1]
        dist = sqrt((player_x - x)**2 + (player_y - y)**2)
        if dist <= 3:
            if random.randint(0,1) == 1:
                if player_x > x:
                    self.x += 1
                elif player_x < x:
                    self.x -= 1
            else:
                if player_y > y:
                    self.y += 1
                elif player_y < y:
                    self.y -= 1

    def looted(self):
        pass

class Bat(Ennemy):
    def __init__(self, position):
        super.__init__(6, 1, position)

    def search_player(self, player):
        super.search_player(player)
    
    def loot(self):
        super.loot()

    
class Snake(Ennemy):
    def __init__(self, position):
        super.__init__(6, 2, position)

    def search_player(self, player):
        super.search_player(player)
    
    def loot(self):
        super.loot()


class Nutria(Ennemy):
    def __init__(self, position):
        super.__init__(8, 2, position)

    def search_player(self, player):
        super.search_player(player)
    
    def loot(self):
        super.loot()

class Squirrel(Ennemy):

    def __init__(self, position):
        super.__init__(6, 4, position)

    def search_player(self, player):
        super.search_player(player)
    
    def loot(self):
        super.loot()

class Minotaur(Ennemy):

    def __init__(self, position):
        super.__init__(15, 6, position)

    def search_player(self, player):
        super.search_player(player)
    
    def loot(self):
        super.loot()

class Dragon(Ennemy):

     def __init__(self, position):
        super.__init__(25, 15, position)

    def search_player(self, player):
        super.search_player(player)
    
    def loot(self):
        super.loot()

    







        