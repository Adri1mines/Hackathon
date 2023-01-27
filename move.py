# Python Standard Library
import copy
import random
import sys

# Third-Party Libraries
import pygame
def move(entity, direction):
    entity.position[0]+=direction[0]
    entity.position[1]+=direction[1]
    return entity
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_DOWN:
                direction = [0, 1]
                if labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == " " or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == "|" or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == "-":
                    pass
                elif labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == "." or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]]= "+" or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]]= "#" or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]]= "=":
                    move(player, direction)
                else:
                    player.battle(labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]])

            if event.key == pygame.K_UP:
                direction = [0, -1]
                if labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == " " or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == "|" or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == "-":
                    pass
                elif labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == "." or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]]= "+" or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]]= "#" or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]]= "=":
                    move(player, direction)
                else:
                    player.battle(labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]])
            if event.key == pygame.K_LEFT:
                direction = [-1, 0] 
                if labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == " " or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == "|" or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == "-":
                    pass
                elif labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == "." or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]]= "+" or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]]= "#" or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]]= "=":
                    move(player, direction)
                else:
                    player.battle(labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]])
            if event.key == pygame.K_RIGHT:
                direction = [1, 0]
                if labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == " " or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == "|" or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == "-":
                    pass
                elif labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]] == "." or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]]= "+" or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]]= "#" or labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]]= "=":
                    move(player, direction)
                else:
                    player.battle(labyrinth[player.position[0]+direction[0]][player.position[1]+direction[1]])
