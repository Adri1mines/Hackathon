# Python Standard Library
import copy
import random
import sys

# Third-Party Libraries
import pygame
def setup():
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    return (screen)

def display(labyrinth):
    
KEY_BINDINGS = {
   "q": exit,
   "up": move(UP),
   "down": move(DOWN),
   "left": move(LEFT),
   "right": move(RIGHT),
#    "s": save_state,
#    "l": load_state,
}
KEY_EVENT_HANDLER = {
   pygame.key.key_code(k): v
   for k, v in KEY_BINDINGS.items()
}

