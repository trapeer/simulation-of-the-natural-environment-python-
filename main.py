from animal import *
import random
import os
import pygame
import time

FOOD_APPEARING_RATE = 0.3
MAP_SIZE = 50
WINDOW_SIZE = 1000
ICON_SIZE = int(WINDOW_SIZE / MAP_SIZE)
SLOW_SIMULATION = False


def draw(animals, simulation_map):
    pygame.event.pump()
    screen.fill(pygame.Color(0, 0, 0))
    for row in range(MAP_SIZE):
        for col in range(MAP_SIZE):
            if simulation_map[row][col].food:
                screen.blit(food_img, (row * ICON_SIZE, col * ICON_SIZE))
    for animal in animals:
        if isinstance(animal, Rabbit) and animal.sex == 0:
            screen.blit(rabbit_female_img, (animal.position_x * ICON_SIZE, animal.position_y * ICON_SIZE))
        elif isinstance(animal, Rabbit) and animal.sex == 1:
            screen.blit(rabbit_male_img, (animal.position_x * ICON_SIZE, animal.position_y * ICON_SIZE))
        elif isinstance(animal, Fox) and animal.sex == 0:
            screen.blit(fox_female_img, (animal.position_x * ICON_SIZE, animal.position_y * ICON_SIZE))
        elif isinstance(animal, Fox) and animal.sex == 1:
            screen.blit(fox_male_img, (animal.position_x * ICON_SIZE, animal.position_y * ICON_SIZE))
    pygame.display.update()


def simulate(animals, simulation_map):
    for row in range(MAP_SIZE):
        for col in range(MAP_SIZE):
            if random.random() <= FOOD_APPEARING_RATE: simulation_map[row][col].food = True
            else: simulation_map[row][col].food = False
    for animal in animals:
        animal.movements = animal.speed
    for move in range(Animal.movements_max):
        draw(animals, simulation_map)
        if SLOW_SIMULATION: time.sleep(1)
        for animal in animals:
            animal.move(simulation_map)
            animal.eat(animals, simulation_map)
            animal.reproduce(animals, simulation_map)
    for animal in range(len(animals) - 1, -1, -1):
        if animals[animal].survive(animals, simulation_map) == 0: del animals[animal]


def get_animals(animals, simulation_map):
    with open("animals.txt") as fp:
        fp.readline()
        while True:
            line = fp.readline()
            if not line: break
            var = line.split()
            if var[0] == 'rabbit':
                Rabbit.number_of_creatures += 1
                animals.append(Rabbit(min(int(var[1]), MAP_SIZE - 1),min(int(var[2]), MAP_SIZE - 1),int(var[3]),int(var[4]),int(var[5]),int(var[6]),int(var[7]),int(var[8]),float(var[9]),int(var[10])))
                if int(var[4]) == 0 : simulation_map[min(int(var[1]), MAP_SIZE - 1)][min(int(var[2]), MAP_SIZE - 1)].rabbit_female += 1
                else: simulation_map[min(int(var[1]), MAP_SIZE - 1)][min(int(var[2]), MAP_SIZE - 1)].rabbit_male += 1
            elif var[0] == 'rabbit_baby':
                animals[len(animals) - 1].unbornBabies.append(Rabbit(int(var[1]),int(var[2]),int(var[3]),int(var[4]),int(var[5]),int(var[6]),int(var[7]),int(var[8]),float(var[9]),int(var[10])))
            elif var[0] == 'fox':
                Fox.number_of_creatures += 1
                animals.append(Fox(min(int(var[1]), MAP_SIZE - 1),min(int(var[2]), MAP_SIZE - 1),int(var[3]),int(var[4]),int(var[5]),int(var[6]),int(var[7]),int(var[8]),float(var[9]),int(var[10])))
                if int(var[4]) == 0 : simulation_map[min(int(var[1]), MAP_SIZE - 1)][min(int(var[2]), MAP_SIZE - 1)].fox_female += 1
                else: simulation_map[min(int(var[1]), MAP_SIZE - 1)][min(int(var[2]), MAP_SIZE - 1)].fox_male += 1
            elif var[0] == 'fox_baby':
                animals[len(animals) - 1].unbornBabies.append(Fox(int(var[1]),int(var[2]),int(var[3]),int(var[4]),int(var[5]),int(var[6]),int(var[7]),int(var[8]),float(var[9]),int(var[10])))
            else: print("error when getting data from file")


def save_animals(animals):
    f = open("tmp.txt", "x")
    f.write('animal_name  pos_x pos_y age sex food_capacity sight_range speed agility reproduction_pro owned_food')
    for animal in animals:
        if isinstance(animal, Rabbit):
            f.write(f"\nrabbit       {animal.position_x:5d} {animal.position_y:5d} {animal.age:3d} {animal.sex:3d} {animal.food_capacity:13d} {animal.sight_range:11d} {animal.speed:5d} {animal.agility:7d} {animal.reproduction_probability:16.2f} {animal.owned_food:10d}")
            for baby in animal.unbornBabies:
                f.write(f"\nrabbit_baby  {baby.position_x:5d} {baby.position_y:5d} {baby.age:3d} {baby.sex:3d} {baby.food_capacity:13d} {baby.sight_range:11d} {baby.speed:5d} {baby.agility:7d} {baby.reproduction_probability:16.2f} {baby.owned_food:10d}")
        if isinstance(animal, Fox):
            f.write(f"\nfox          {animal.position_x:5d} {animal.position_y:5d} {animal.age:3d} {animal.sex:3d} {animal.food_capacity:13d} {animal.sight_range:11d} {animal.speed:5d} {animal.agility:7d} {animal.reproduction_probability:16.2f} {animal.owned_food:10d}")
            for baby in animal.unbornBabies:
                f.write(f"\nfox_baby     {baby.position_x:5d} {baby.position_y:5d} {baby.age:3d} {baby.sex:3d} {baby.food_capacity:13d} {baby.sight_range:11d} {baby.speed:5d} {baby.agility:7d} {baby.reproduction_probability:16.2f} {baby.owned_food:10d}")
    f.close()
    os.remove("animals.txt")
    os.renames("tmp.txt", "animals.txt")


class Map_piece():
    def __init__(self):
        self.food = False
        self.rabbit_male = 0
        self.rabbit_female = 0
        self.fox_male = 0
        self.fox_female = 0



pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("simulation")
rabbit_male_img = pygame.image.load('assets\\rabbit_male.png')
rabbit_male_img = pygame.transform.scale(rabbit_male_img, (ICON_SIZE, ICON_SIZE))
rabbit_female_img = pygame.image.load('assets\\rabbit_female.png')
rabbit_female_img = pygame.transform.scale(rabbit_female_img,(ICON_SIZE, ICON_SIZE))
fox_male_img = pygame.image.load('assets\\fox_male.png')
fox_male_img = pygame.transform.scale(fox_male_img, (ICON_SIZE, ICON_SIZE))
fox_female_img = pygame.image.load('assets\\fox_female.png')
fox_female_img = pygame.transform.scale(fox_female_img, (ICON_SIZE, ICON_SIZE))
food_img = pygame.image.load('assets\\food.png')
food_img = pygame.transform.scale(food_img, (ICON_SIZE, ICON_SIZE))

animals = []
simulation_map = [[0] * MAP_SIZE for i in range(MAP_SIZE)]
for row in range(MAP_SIZE):
    for col in range(MAP_SIZE):
        simulation_map[row][col] = Map_piece()
get_animals(animals, simulation_map)
rabbit_number_start, fox_number_start = Rabbit.number_of_creatures, Fox.number_of_creatures
while True:
    print("how many rounds do you want to simulate?")
    number_of_rounds = int(input())
    for round in range(number_of_rounds):
        simulate(animals, simulation_map)
        rabbit_number_finish, fox_number_finish = Rabbit.number_of_creatures, Fox.number_of_creatures
        print(f"round {round + 1:3d}  |  start: rabbits = {rabbit_number_start:5d} foxes = {fox_number_start:5d}   |   finish: rabbits = {rabbit_number_finish:5d} foxes = {fox_number_finish:5d}")
        rabbit_number_start, fox_number_start = Rabbit.number_of_creatures, Fox.number_of_creatures
    save_animals(animals)
