import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def __init__(self):
        super().__init__()

    def append(self, item) -> None:
        self.log(f"{item} was added")
        super().append(item)


if __name__ == "__main__":
    some_lst = []
    ll = LoggableList()
    LoggableList.append(ll, 5)
    LoggableList.append(ll, 'some_Str')
    LoggableList.append(ll, [3, 6])
    LoggableList.append(ll, (1, 2, 3, 4))
    print(ll)
