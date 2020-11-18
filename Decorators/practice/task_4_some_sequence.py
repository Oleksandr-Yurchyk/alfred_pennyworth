def calc(number: int):
    lst = []
    for i in range(1, number + 1):
        counter = 0
        while counter != i:
            if len(lst) == number:
                break
            counter += 1
            print(i, end=' ')
            lst.append(i)


calc(7)
