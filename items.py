# Python Standard Library
import copy
import random
import sys

# Third-Party Libraries
import pygame
class items:
    def __init__(self, position, value=0, name= None,target=None):
        self.value= value
        self.name = name
        self.position = position 
        self.target = target
    def use_item(self,player):
        if self.name == "potion" and player[self.name]>0:
            self.target.hp+= self.value
            player.inventory[self.name]-=1