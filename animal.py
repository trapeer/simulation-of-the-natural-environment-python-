import random



class Animal:
    movements_max = 0

    def __init__(self, position_x=0, position_y=0, age=-1, sex=0, food_capacity=0, sight_range=0, speed=0, agility=0,  reproduction_probability=0.5, owned_food=0):
        self.position_x = position_x
        self.position_y = position_y
        self.age = age
        self.sex = sex
        self.food_capacity = food_capacity
        self.sight_range = sight_range
        self.speed = speed
        self.movements = speed
        self.agility = agility
        self.reproduction_probability = reproduction_probability
        self.owned_food = owned_food
        self.unbornBabies = []
        if self.speed > Animal.movements_max:
            Animal.movements_max = self.speed

    def move_right(self, simulation_map):
        if isinstance(self, Rabbit):
            if self.sex == 0:
                simulation_map[self.position_x][self.position_y].rabbit_female -= 1
                simulation_map[self.position_x + 1][self.position_y].rabbit_female += 1
            else:
                simulation_map[self.position_x][self.position_y].rabbit_male -= 1
                simulation_map[self.position_x + 1][self.position_y].rabbit_male += 1
        if isinstance(self, Fox):
            if self.sex == 0:
                simulation_map[self.position_x][self.position_y].fox_female -= 1
                simulation_map[self.position_x + 1][self.position_y].fox_female += 1
            else:
                simulation_map[self.position_x][self.position_y].fox_male -= 1
                simulation_map[self.position_x + 1][self.position_y].fox_male += 1
        self.position_x += 1

    def move_left(self, simulation_map):
        if isinstance(self, Rabbit):
            if self.sex == 0:
                simulation_map[self.position_x][self.position_y].rabbit_female -= 1
                simulation_map[self.position_x - 1][self.position_y].rabbit_female += 1
            else:
                simulation_map[self.position_x][self.position_y].rabbit_male -= 1
                simulation_map[self.position_x - 1][self.position_y].rabbit_male += 1
        if isinstance(self, Fox):
            if self.sex == 0:
                simulation_map[self.position_x][self.position_y].fox_female -= 1
                simulation_map[self.position_x - 1][self.position_y].fox_female += 1
            else:
                simulation_map[self.position_x][self.position_y].fox_male -= 1
                simulation_map[self.position_x - 1][self.position_y].fox_male += 1
        self.position_x -= 1

    def move_up(self, simulation_map):
        if isinstance(self, Rabbit):
            if self.sex == 0:
                simulation_map[self.position_x][self.position_y].rabbit_female -= 1
                simulation_map[self.position_x][self.position_y + 1].rabbit_female += 1
            else:
                simulation_map[self.position_x][self.position_y].rabbit_male -= 1
                simulation_map[self.position_x][self.position_y + 1].rabbit_male += 1
        if isinstance(self, Fox):
            if self.sex == 0:
                simulation_map[self.position_x][self.position_y].fox_female -= 1
                simulation_map[self.position_x][self.position_y + 1].fox_female += 1
            else:
                simulation_map[self.position_x][self.position_y].fox_male -= 1
                simulation_map[self.position_x][self.position_y + 1].fox_male += 1
        self.position_y += 1

    def move_down(self, simulation_map):
        if isinstance(self, Rabbit):
            if self.sex == 0:
                simulation_map[self.position_x][self.position_y].rabbit_female -= 1
                simulation_map[self.position_x][self.position_y - 1].rabbit_female += 1
            else:
                simulation_map[self.position_x][self.position_y].rabbit_male -= 1
                simulation_map[self.position_x][self.position_y - 1].rabbit_male += 1
        if isinstance(self, Fox):
            if self.sex == 0:
                simulation_map[self.position_x][self.position_y].fox_female -= 1
                simulation_map[self.position_x][self.position_y - 1].fox_female += 1
            else:
                simulation_map[self.position_x][self.position_y].fox_male -= 1
                simulation_map[self.position_x][self.position_y - 1].fox_male += 1
        self.position_y -= 1


class Rabbit(Animal):
    number_of_creatures = 0
    def __init__(self, position_x=0, position_y=0, age=-1, sex=0, food_capacity=0, sight_range=0, speed=0, agility=0,  reproduction_probability=0.5, owned_food=0):
        super(Rabbit, self).__init__(position_x, position_y, age, sex, food_capacity, sight_range, speed, agility,  reproduction_probability, owned_food)

    def move(self, simulation_map):
        if self.movements == 0: return
        self.movements -= 1
        nearest_predator = {'x': 1000, 'y': 1000}
        nearest_animal_to_breed = {'x': 1000, 'y': 1000}
        nearest_food = {'x': 1000, 'y': 1000}
        for col in range(self.sight_range*(-1), self.sight_range):
            for row in range(self.sight_range*(-1), self.sight_range):
                if self.position_x + col < 0 or self.position_x + col >= len(simulation_map) or self.position_y + row < 0 or self.position_y + row >= len(simulation_map):
                    continue
                if simulation_map[self.position_x + col][self.position_y + row].food and abs(col) + abs(row) < abs(nearest_food['x']) + abs(nearest_food['y']):
                    nearest_food['x'] = col
                    nearest_food['y'] = row
                if simulation_map[self.position_x + col][self.position_y + row].fox_male + simulation_map[self.position_x + col][self.position_y + row].fox_female > 0 and abs(col) + abs(row) < abs(nearest_predator['x']) + abs(nearest_predator['y']):
                    nearest_predator['x'] = col
                    nearest_predator['y'] = row
                if self.sex == 0 and len(self.unbornBabies) == 0:
                    if simulation_map[self.position_x + col][self.position_y + row].rabbit_male > 0 and abs(col) + abs(row) < abs(nearest_animal_to_breed['x']) + abs(nearest_animal_to_breed['y']):
                        nearest_animal_to_breed['x'] = col
                        nearest_animal_to_breed['y'] = row
                if self.sex == 1:
                    if simulation_map[self.position_x + col][self.position_y + row].rabbit_female > 0 and abs(col) + abs(row) < abs(nearest_animal_to_breed['x']) + abs(nearest_animal_to_breed['y']):
                        nearest_animal_to_breed['x'] = col
                        nearest_animal_to_breed['y'] = row
        if abs(nearest_predator['x']) + abs(nearest_predator['y']) <= 3:
            if nearest_predator['x'] > 0 and self.position_x > 0: self.move_left(simulation_map)
            elif nearest_predator['x'] < 0 and self.position_x + 1 < len(simulation_map): self.move_right(simulation_map)
            elif nearest_predator['y'] < 0 and self.position_y + 1 < len(simulation_map): self.move_up(simulation_map)
            else:
                if self.position_y > 0: self.move_down(simulation_map)
        elif self.owned_food <= 2 and nearest_food['x'] < 100:
            if nearest_food['x'] > 0: self.move_right(simulation_map)
            elif nearest_food['x'] < 0: self.move_left(simulation_map)
            elif nearest_food['y'] > 0: self.move_up(simulation_map)
            elif nearest_food['y'] < 0 : self.move_down(simulation_map)
        elif nearest_animal_to_breed['x'] < 100:
            if nearest_animal_to_breed['x'] > 0: self.move_right(simulation_map)
            elif nearest_animal_to_breed['x'] < 0: self.move_left(simulation_map)
            elif nearest_animal_to_breed['y'] > 0: self.move_up(simulation_map)
            elif nearest_animal_to_breed['y'] < 0 : self.move_down(simulation_map)
        else:
            rand = random.randint(0,3)
            if rand == 0 and self.position_x + 1 < len(simulation_map): self.move_right(simulation_map)
            elif rand == 1 and self.position_x > 0: self.move_left(simulation_map)
            elif rand == 2 and self.position_y + 1 < len(simulation_map): self.move_up(simulation_map)
            elif rand == 3 and self.position_y > 0: self.move_down(simulation_map)

    def eat(self, animals, simulation_map):
        if simulation_map[self.position_x][self.position_y].food:
            if self.owned_food < self.food_capacity:
                simulation_map[self.position_x][self.position_y].food = False
                self.owned_food += 1

    def reproduce(self, animals, simulation_map):
        if self.sex != 0 or self.owned_food <= 1 or len(self.unbornBabies) > 0:
            return
        if simulation_map[self.position_x][self.position_y].rabbit_male <= 0:
            return
        for animal in animals:
            if isinstance(animal, Rabbit) and animal.sex == 1 and animal.owned_food > 0 and animal.position_x == self.position_x and animal.position_y == self.position_y:
                if random.randint(0,99) < 50*(animal.reproduction_probability + self.reproduction_probability):
                    self.owned_food -=1
                    age = -2
                    sex = random.randint(0,1)
                    if random.randint(0,1) == 0: food_capacity = self.food_capacity
                    else: food_capacity = animal.food_capacity
                    if random.randint(0,9) == 0: food_capacity +=1
                    elif random.randint(0,9) == 0: food_capacity -=1
                    if random.randint(0,1) == 0: sight_range = self.sight_range
                    else: sight_range = animal.sight_range
                    if random.randint(0,9) == 0: sight_range +=1
                    elif random.randint(0,9) == 0: sight_range -=1
                    if random.randint(0,1) == 0: speed = self.speed
                    else: speed = animal.speed
                    if random.randint(0,9) == 0: speed +=1
                    elif random.randint(0,9) == 0: speed -=1
                    if random.randint(0,1) == 0: agility = self.agility
                    else: agility = animal.agility
                    if random.randint(0,9) == 0: agility +=1
                    elif random.randint(0,9) == 0: agility -=1
                    if random.randint(0,1) == 0: reproduction_probability = self.reproduction_probability
                    else: reproduction_probability = animal.reproduction_probability
                    if random.randint(0,9) == 0: reproduction_probability +=0.02
                    elif random.randint(0,9) == 0: reproduction_probability -=0.02
                    if food_capacity < 0: food_capacity = 0
                    if sight_range < 0: sight_range = 0
                    if speed < 0: speed = 0
                    if agility < 0: agility = 0
                    if reproduction_probability < 0: reproduction_probability = 0
                    if reproduction_probability > 1: reproduction_probability = 1
                    while food_capacity + sight_range + speed + agility > 15:  # ograniczenie maksymalnych statystyk
                        rand = random.randint(0, 3)
                        if rand == 0 and food_capacity > 0: food_capacity -= 1
                        elif rand == 1 and sight_range > 0: sight_range -= 1
                        elif rand == 2 and speed > 0: speed -= 1
                        elif rand == 3 and agility > 0: agility -= 1
                    self.unbornBabies.append(Rabbit(0,0,age,sex,food_capacity,sight_range,speed,agility,reproduction_probability,owned_food=1))
                    return
                else: return

    def survive(self, animals, simulation_map): #return = 0 - death 1 - survive
        for babie in range(len(self.unbornBabies) - 1, -1, -1):
            self.unbornBabies[babie].age += 1
            if self.unbornBabies[babie].age >= 0:
                self.unbornBabies[babie].position_x = self.position_x
                self.unbornBabies[babie].position_y = self.position_y
                if self.unbornBabies[babie].sex == 0:
                    simulation_map[self.position_x][self.position_y].rabbit_female += 1
                else:
                    simulation_map[self.position_x][self.position_y].rabbit_male += 1
                animals.append(self.unbornBabies[babie])
                Rabbit.number_of_creatures += 1
                del self.unbornBabies[babie]
        self.age += 1
        if self.owned_food == 0 and random.randint(0,1) == 0:
            if self.sex == 0:
                simulation_map[self.position_x][self.position_y].rabbit_female -= 1
            else:
                simulation_map[self.position_x][self.position_y].rabbit_male -= 1
            Rabbit.number_of_creatures -= 1
            return 0
        if self.owned_food > 0:
            self.owned_food-=1
        if self.age > 20 and random.randint(0,4) == 0:
            if self.sex == 0:
                simulation_map[self.position_x][self.position_y].rabbit_female -= 1
            else:
                simulation_map[self.position_x][self.position_y].rabbit_male -= 1
            Rabbit.number_of_creatures -= 1
            return 0
        return 1


class Fox(Animal):
    number_of_creatures = 0
    def __init__(self, position_x=0, position_y=0, age=-1, sex=0, food_capacity=0, sight_range=0, speed=0, agility=0,  reproduction_probability=0.5, owned_food=0):
        super(Fox, self).__init__(position_x, position_y, age, sex, food_capacity, sight_range, speed, agility,  reproduction_probability, owned_food)

    def move(self, simulation_map):
        if self.movements == 0: return
        self.movements -= 1
        nearest_animal_to_breed = {'x': 1000, 'y': 1000}
        nearest_food = {'x': 1000, 'y': 1000}
        for col in range(self.sight_range * (-1), self.sight_range):
            for row in range(self.sight_range * (-1), self.sight_range):
                if self.position_x + col < 0 or self.position_x + col >= len(simulation_map) or self.position_y + row < 0 or self.position_y + row >= len(simulation_map):
                    continue
                if simulation_map[self.position_x + col][self.position_y + row].rabbit_male + simulation_map[self.position_x + col][self.position_y + row].rabbit_female > 0 and abs(col) + abs(row) < abs(nearest_food['x']) + abs(nearest_food['y']):
                    nearest_food['x'] = col
                    nearest_food['y'] = row
                if self.sex == 0 and len(self.unbornBabies) == 0:
                    if simulation_map[self.position_x + col][self.position_y + row].fox_male > 0 and abs(col) + abs(row) < abs(nearest_animal_to_breed['x']) + abs(nearest_animal_to_breed['y']):
                        nearest_animal_to_breed['x'] = col
                        nearest_animal_to_breed['y'] = row
                if self.sex == 1:
                    if simulation_map[self.position_x + col][self.position_y + row].fox_female > 0 and abs(col) + abs(row) < abs(nearest_animal_to_breed['x']) + abs(nearest_animal_to_breed['y']):
                        nearest_animal_to_breed['x'] = col
                        nearest_animal_to_breed['y'] = row
        if self.owned_food <= 2 and nearest_food['x'] < 100:
            if nearest_food['x'] > 0: self.move_right(simulation_map)
            elif nearest_food['x'] < 0: self.move_left(simulation_map)
            elif nearest_food['y'] > 0: self.move_up(simulation_map)
            elif nearest_food['y'] < 0: self.move_down(simulation_map)
        elif nearest_animal_to_breed['x'] < 100:
            if nearest_animal_to_breed['x'] > 0: self.move_right(simulation_map)
            elif nearest_animal_to_breed['x'] < 0: self.move_left(simulation_map)
            elif nearest_animal_to_breed['y'] > 0: self.move_up(simulation_map)
            elif nearest_animal_to_breed['y'] < 0: self.move_down(simulation_map)
        else:
            rand = random.randint(0, 3)
            if rand == 0 and self.position_x + 1 < len(simulation_map):
                self.move_right(simulation_map)
            elif rand == 1 and self.position_x > 0:
                self.move_left(simulation_map)
            elif rand == 2 and self.position_y + 1 < len(simulation_map):
                self.move_up(simulation_map)
            elif rand == 3 and self.position_y > 0:
                self.move_down(simulation_map)

    def eat(self, animals, simulation_map):
        if simulation_map[self.position_x][self.position_y].rabbit_male + simulation_map[self.position_x][self.position_y].rabbit_female <= 0:
            return
        for animal in range(len(animals) - 1, -1, -1):
            if isinstance(animals[animal], Rabbit) and self.position_y == animals[animal].position_y and self.position_x == animals[animal].position_x:
                if random.randint(0,9) + self.agility - animals[animal].agility >= 8:
                    self.owned_food += 3 + int(animals[animal].owned_food/2)
                    if animals[animal].sex == 0:
                        simulation_map[animals[animal].position_x][animals[animal].position_y].rabbit_female -= 1
                    else:
                        simulation_map[animals[animal].position_x][animals[animal].position_y].rabbit_male -= 1
                    Rabbit.number_of_creatures -= 1
                    del animals[animal]
                    if self.owned_food > self.food_capacity:
                        self.owned_food = self.food_capacity
                else: return

    def reproduce(self, animals, simulation_map):
        if self.sex != 0 or self.owned_food <= 2 or len(self.unbornBabies) > 0:
            return
        if simulation_map[self.position_x][self.position_y].fox_male <= 0:
            return
        for animal in animals:
            if isinstance(animal, Fox) and animal.sex == 1 and animal.owned_food > 0 and animal.position_x == self.position_x and animal.position_y == self.position_y:
                if random.randint(0, 99) < 50 * (animal.reproduction_probability + self.reproduction_probability):
                    self.owned_food -= 2
                    age = -4
                    sex = random.randint(0, 1)
                    if random.randint(0, 1) == 0: food_capacity = self.food_capacity
                    else: food_capacity = animal.food_capacity
                    if random.randint(0, 9) == 0: food_capacity += 1
                    elif random.randint(0, 9) == 0: food_capacity -= 1
                    if random.randint(0, 1) == 0: sight_range = self.sight_range
                    else: sight_range = animal.sight_range
                    if random.randint(0, 9) == 0: sight_range += 1
                    elif random.randint(0, 9) == 0: sight_range -= 1
                    if random.randint(0, 1) == 0: speed = self.speed
                    else: speed = animal.speed
                    if random.randint(0, 9) == 0: speed += 1
                    elif random.randint(0, 9) == 0: speed -= 1
                    if random.randint(0, 1) == 0: agility = self.agility
                    else: agility = animal.agility
                    if random.randint(0, 9) == 0: agility += 1
                    elif random.randint(0, 9) == 0: agility -= 1
                    if random.randint(0, 1) == 0: reproduction_probability = self.reproduction_probability
                    else: reproduction_probability = animal.reproduction_probability
                    if random.randint(0, 9) == 0: reproduction_probability += 0.02
                    elif random.randint(0, 9) == 0: reproduction_probability -= 0.02
                    if food_capacity < 0: food_capacity = 0
                    if sight_range < 0: sight_range = 0
                    if speed < 0: speed = 0
                    if agility < 0: agility = 0
                    if reproduction_probability < 0: reproduction_probability = 0
                    if reproduction_probability > 1: reproduction_probability = 1
                    while food_capacity + sight_range + speed + agility > 20:  # ograniczenie maksymalnych statystyk
                        rand = random.randint(0, 3)
                        if rand == 0 and food_capacity > 0: food_capacity -= 1
                        elif rand == 1 and sight_range > 0: sight_range -= 1
                        elif rand == 2 and speed > 0: speed -= 1
                        elif rand == 3 and agility > 0: agility -= 1
                    self.unbornBabies.append(Fox(0, 0, age, sex, food_capacity, sight_range, speed, agility, reproduction_probability,owned_food=1))
                    return
                else:
                    return

    def survive(self, animals, simulation_map): #return = 0 - death 1 - survive
        for babie in range(len(self.unbornBabies) - 1, -1, -1):
            self.unbornBabies[babie].age += 1
            if self.unbornBabies[babie].age >= 0:
                self.unbornBabies[babie].position_x = self.position_x
                self.unbornBabies[babie].position_y = self.position_y
                if self.unbornBabies[babie].sex == 0:
                    simulation_map[self.position_x][self.position_y].fox_female += 1
                else:
                    simulation_map[self.position_x][self.position_y].fox_male += 1
                Fox.number_of_creatures += 1
                animals.append(self.unbornBabies[babie])
                del self.unbornBabies[babie]
        self.age += 1
        if self.owned_food == 0 and random.randint(0, 2) == 0:
            if self.sex == 0:
                simulation_map[self.position_x][self.position_y].fox_female -= 1
            else:
                simulation_map[self.position_x][self.position_y].fox_male -= 1
            Fox.number_of_creatures -= 1
            return 0
        if self.owned_food > 0:
            self.owned_food -= 1
        if self.age > 20 and random.randint(0, 4) == 0:
            if self.sex == 0:
                simulation_map[self.position_x][self.position_y].fox_female -= 1
            else:
                simulation_map[self.position_x][self.position_y].fox_male -= 1
            Fox.number_of_creatures -= 1
            return 0
        return 1
