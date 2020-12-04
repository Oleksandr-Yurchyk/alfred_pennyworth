import json


with open('animals.json', 'r') as f:
    json_data = json.load(f)
    json_data = json_data['animals']
    print(json_data)


class Animal:
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

    def __str__(self):
        return f"Animal {self.power} {self.speed}"

    def __repr__(self):
        return f"Animal {self.power} {self.speed}"


true_animals = [Animal(power=i['power'], speed=i['speed']) for i in json_data]
print(true_animals)
