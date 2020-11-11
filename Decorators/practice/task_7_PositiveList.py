class PositiveList(list):
    def __init__(self):
        super().__init__()

    def append(self, number) -> None:
        if number > 0 and isinstance(number, int):
            super().append(number)
        else:
            raise NonPositiveError("Wrong argument for this method, expected integer positive number")


class NonPositiveError(Exception):
    pass


if __name__ == "__main__":
    pl = PositiveList()
    PositiveList.append(pl, 10)  # Will add 10 to list
    PositiveList.append(pl, 0)  # Will raise NonPositiveError
    PositiveList.append(pl, 3)  # Will add 3 to list
    PositiveList.append(pl, -7)  # Will raise NonPositiveError
    print(pl)
