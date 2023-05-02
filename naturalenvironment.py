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

        self.pos = pygame.Rect(WIDTH/2, HEIGHT/2, PLAYERWIDTH, PLAYERWIDTH)
        self.x = int(WIDTH/2)
        self.y = int(HEIGHT/2)

    def move(self, dx, dy):
        self.pos.centerx += dx
        self.pos.centery += dy
        
        

    def display(self, color=(255,0,0)):
        pygame.draw.rect(surface, color, self.pos)

red = (255,0,0)
lime_green = (100,255,100)


# Initializing Pygame
pygame.init()
clock = pygame.time.Clock()
dt = 5

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

        surface.fill([0,0,0])
        for food in food_pool:
            #pygame.draw.rect(surface, (0,255,255), pygame.Rect(food[0], food[1], 10, 10 ))
            pygame.draw.circle(surface, lime_green, [food[0], food[1]], FOODRADIUS)

        for pop_index, player in enumerate(player_pool):
            colour = (100,0,0)
            for food_index, food in enumerate(food_pool):
                #if (food[0] - player.x) ** 2 +  (food[1] - player.y) ** 2 < 40:
                
                if math.sqrt((player.pos.centerx - food[0]) ** 2 + (player.pos.centery - food[1]) ** 2) < FOODRADIUS + PLAYERWIDTH:#player.pos.collidepoint(food):
                    fitness_values[pop_index] -= 50000 * (1-tick/700)
                    colour = (0,0,200)
                    #food_pool[food_index] = (random.random() * WIDTH, random.random() * HEIGHT)

            # check bounds
            if player.pos.centerx > WIDTH or player.pos.centerx < 0 or player.pos.centery > HEIGHT or player.pos.centery < 0:
                fitness_values[pop_index] += 0
            else:
                fitness_values[pop_index] += 1
                input_layer = food_pool

                input_layer = list(np.array(input_layer).flatten())
                input_layer.append(player.pos.centerx)
                input_layer.append(player.pos.centery)
                #stuff_abdullah_wants_to_give_it = [500]
                #for stuff in stuff_abdullah_wants_to_give_it:
                #    input_layer.append(stuff)
                #input_layer = [x / WIDTH for x in list(input_layer)]

                """
                for p in player_pool:
                    input_layer.append(p.pos.centerx)
                    input_layer.append(p.pos.centery)
                """

                #print(input_layer)

                velocity = population[pop_index].inference(input_layer)
                player.move(velocity[0] * dt, velocity[1] * dt)
                if pop_index == pop_size-1:
                    player.display()
                else:
                    player.display(colour)


        pygame.display.flip()

    return fitness_values

    
# 527