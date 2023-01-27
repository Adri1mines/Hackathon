# Python Standard Library
import copy
import random
import sys

# Third-Party Libraries
import pygame


#KEY_BINDINGS = {
#    "q": exit,
#    "up": move(UP),
#    "down": move(DOWN),
#    "left": move(LEFT),
#    "right": move(RIGHT),
#    "s": save_state,
#    "l": load_state,
#}
#KEY_EVENT_HANDLER = {
#    pygame.key.key_code(k): v
#    for k, v in KEY_BINDINGS.items()
#}

class Player:
    def __init__(self, position, level=1, exp=0, exp_up= 12, gold=0, hp_max=12, atk = 3, inventory = {"swords": 0, "potions": 0} ):
        self.position = position
        self.level = level
        self.exp = exp
        self.exp_up = exp_up*level
        self.gold = gold
        self.hp_max = hp_max + hp_max*(level-1)/2
        self.hp = copy.copy(hp_max)
        self.atk = atk + level - 1 
        self.base_exp = copy.copy(exp_up)
        self.base_hp = copy.copy(hp_max)
        self.inventory = inventory 
    def get_base_exp(self):
        return copy.copy(self.base_exp)
    base_exp = property(get_base_exp)
    def get_base_hp(self):
        return copy.copy(self.base_hp)
    base_hp = property(get_base_hp)
    def get_position(self):
        return copy.copy(self.position)
    position = property(get_position)
    def lv_up(self):
        if self.exp > self.exp_up:
            self.level+=1
            self.exp_up = self.base_exp * self.level
            self.atk += 1
            self.hp_max+= self.base_hp/2
            self.hp = self.hp_max
        else:
            pass
    def battle(self,enemy):
        roll = random.random()
        if roll > 0.5 :
            enemy.hp -= self.atk
            if enemy.hp <= 0 :
                self.exp += enemy.exp
                self.lv_up(self)
        else:
            self.hp -= enemy.atk
            if self.hp <= 0 :
                exit()
    def loot_item(item, self):
        if item.name == "gold":
            self.gold += item.value
        elif item.name == "sword":
            self.atk += item.value
        elif item.name == "potion":
            self.inventory["potions"]+=1

    





