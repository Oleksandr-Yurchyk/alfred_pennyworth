TROLL_TAX = 50


class Person:
    def __init__(self, name: str, money: int):
        self.name = name
        self.money = money


def troll(func):
    def inner(*args, **kwargs):
        person = args[0]
        print(person)
        if person.money >= TROLL_TAX:
            person.money -= TROLL_TAX
        else:
            raise TrollIsAngry
        print(person.money)
        print("Troll is checking person money")

        return func(*args, **kwargs)
    return inner


@troll
def bridge(pers: Person):
    print(f"Person passed the bridge with money: {pers.money}")
    return None


class TrollIsAngry(Exception):
    pass


if __name__ == "__main__":
    dmytro = Person("Alex", money=100)
    bridge(dmytro)

