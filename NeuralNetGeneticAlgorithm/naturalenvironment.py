# Importing the library
import pygame
from individual import Individual
import random
import numpy as np
from collisions import collision
import math

WIDTH, HEIGHT = 500, 500
FOODRADIUS = 20
PLAYERWIDTH = 10
class Player():
    def __init__(self):

        self.x = random.random() * WIDTH
        self.y = random.random() * HEIGHT
        self.pos = pygame.Rect(self.x, self.y, PLAYERWIDTH, PLAYERWIDTH)
        

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.pos.centerx += dx
        self.pos.centery += dy
        
        

    def display(self, color=(255,0,0)):
        pygame.draw.rect(surface, color, self.pos)

red = (255,0,0)
lime_green = (100,255,100)


# Initializing Pygame
pygame.init()
clock = pygame.time.Clock()
dt = 1

DISPLAY_STUF = True
# Initializing surface
surface = pygame.display.set_mode((WIDTH, HEIGHT))
def find_fitness(population):
    pop_size = len(population)
    food_pool = [[random.random() * WIDTH, random.random() * HEIGHT] for i in range(1)]

    player_pool = [Player() for x in range(pop_size)]
    fitness_values = [0 for x in player_pool]
    
    for tick in range(200):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        if (DISPLAY_STUF):
            surface.fill([0,0,0])
            for food in food_pool:
                #pygame.draw.rect(surface, (0,255,255), pygame.Rect(food[0], food[1], 10, 10 ))
                pygame.draw.circle(surface, lime_green, [food[0], food[1]], FOODRADIUS)

        for pop_index, player in enumerate(player_pool):
            colour = (100,0,0)
            for food_index, food in enumerate(food_pool):
                #if (food[0] - player.x) ** 2 +  (food[1] - player.y) ** 2 < 40:
                
                dist = math.sqrt((player.pos.centerx - food[0]) ** 2 + (player.pos.centery - food[1]) ** 2)
                #fitness_values[pop_index] = 1/ (dist / WIDTH)
                if dist < FOODRADIUS + PLAYERWIDTH:#player.pos.collidepoint(food):
                    colour = (0,0,200)
                    fitness_values[pop_index] += 10
                    #food_pool[food_index] = (random.random() * WIDTH, random.random() * HEIGHT)

            # check bounds
            if player.pos.centerx > WIDTH or player.pos.centerx < 0 or player.pos.centery > HEIGHT or player.pos.centery < 0:
                fitness_values[pop_index] -= 0
            else:
                fitness_values[pop_index] += 0
                input_layer = food_pool

                input_layer = list(np.array(input_layer).flatten())
                input_layer.append(player.x)
                input_layer.append(player.y)
                input_layer = [x/WIDTH for x in input_layer]

                velocity = population[pop_index].activate(input_layer)
                if sum(velocity) == 0:
                    fitness_values[pop_index] -= 100

                player.move(velocity[0] * dt - velocity[1] * dt, velocity[2] * dt - velocity[3] * dt)
                if (DISPLAY_STUF):
                    if pop_index == pop_size-1:
                        player.display()
                    else:
                        player.display(colour)


        if (DISPLAY_STUF):
            pygame.display.flip()

    return fitness_values

    
# 527