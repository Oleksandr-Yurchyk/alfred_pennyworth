from __future__ import annotations
import csv
import logging
import uuid
from random import randint, choice
from abc import ABC, abstractmethod
from pprint import pprint
from typing import Dict

logger = logging.getLogger("Jungle_logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d %b %y, %H:%M:%S')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = str(uuid.uuid4())
        self.max_power = power
        self._current_power = power
        self.speed = speed

    @property
    def current_power(self):
        return self._current_power

    @current_power.setter
    def current_power(self, power):
        if power > self.max_power:
            self._current_power = self.max_power
        else:
            self._current_power = power

    @abstractmethod
    def eat(self, jungle: Jungle):
        raise NotImplementedError

    def has_not_power_to_search_food(self):
        return self.current_power <= 0

    def loss_power(self):
        self.current_power -= int(self.max_power * 0.3)

    def gain_power(self):
        self.current_power += int(self.max_power * 0.4)


class Predator(Animal):

    def eat(self, jungle: Jungle):
        if self.has_not_power_to_search_food():
            jungle.remove_animal(self)
            return

        rand_animal = choice(list(jungle.animals.values()))
        if self.id == rand_animal.id:
            logger.info("Predator catch himself")
            self.loss_power()
            return
        if self.speed > rand_animal.speed and self.current_power > rand_animal.current_power:
            logger.info(f"Predator ate --> {rand_animal.__class__.__name__} <--")
            jungle.remove_animal(rand_animal)
            logger.info("Predator get 40% power")
            self.gain_power()
        else:
            logger.info("Predator did`nt catch anyone")
            self.loss_power()
            rand_animal.loss_power()


class Herbivorous(Animal):

    def eat(self, jungle: Jungle):
        if self.has_not_power_to_search_food():
            jungle.remove_animal(self)
        else:
            logger.info("Herbivorous get 40% power")
            self.gain_power()


class Jungle:

    def __init__(self):
        self.animals: Dict[str, Animal] = dict()
        self.number = -1

    def __getitem__(self, item):
        length = len(self.animals)
        if self.number >= length - 1:
            self.number = -1
            raise StopIteration
        self.number += 1
        return list(self.animals.values())[self.number]

    def add_animal(self, animal: Animal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal: Animal):
        self.animals.pop(animal.id)

    def any_predator_left(self):
        if any(isinstance(obj, Predator) for obj in self.animals.values()):
            return True
        return False


def object_info():
    lst = []
    for id, obj in jungle.animals.items():
        list_animals = [f"{obj.__class__.__name__:11}", f"{obj.max_power}", f"{obj.speed}", f"{obj.id}"]
        lst.append(list_animals)
    pprint(lst)
    return lst


def convert_to_csv():
    with open("animal_in.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(['class', 'power', 'speed', 'id'])
        writer.writerows(object_info())
    print("Wrote info about animal in separate file")


def animal_generator():
    while True:
        if randint(0, 1) == 0:
            yield Predator(power=randint(20, 100), speed=randint(20, 100))
        else:
            yield Herbivorous(power=randint(20, 100), speed=randint(20, 100))


if __name__ == "__main__":
    jungle = Jungle()

    # Creating animal generator
    animal_gen = animal_generator()

    # Add animals to jungle
    for i in range(10):
        jungle.add_animal(next(animal_gen))

    # Converting animals to animal_in.csv
    convert_to_csv()

    # object_info()

    while True:
        if not jungle.any_predator_left():
            logger.info("All Predators died")
            logger.info("--------- Game Over ---------")
            break
        for animal in jungle:
            animal.eat(jungle=jungle)

    # object_info()
