from typing import List


def calculate_ships(data: List[List[int]]):
    count_of_ships = 0
    row = len(data)
    col = len(data[0])

    for i in range(row):
        for j in range(col):
            if i < row - 1 and data[i][j] == 1 and data[i + 1][j] == 1:
                if i < row - 2 and data[i + 2][j] == 1:
                    count_of_ships += 1
                    data[i][j] = 0
                    data[i + 1][j] = 0
                    data[i + 2][j] = 0
                    continue
                count_of_ships += 1
                data[i][j] = 0
                data[i + 1][j] = 0
                continue
    for i in range(row):
        for j in range(col):
            if data[i][j] == 1:
                if j < col - 1 and data[i][j + 1] == 1:
                    if data[i][j + 2] == 1:
                        if data[i][j + 3] == 1:
                            count_of_ships += 1
                            data[i][j] = 0
                            data[i][j + 1] = 0
                            data[i][j + 2] = 0
                            data[i][j + 3] = 0
                            continue
                        count_of_ships += 1
                        data[i][j] = 0
                        data[i][j + 1] = 0
                        data[i][j + 2] = 0
                        continue
                    count_of_ships += 1
                    data[i][j] = 0
                    data[i][j + 1] = 0
                    continue
                count_of_ships += 1
                data[i][j] = 0
                continue
    return count_of_ships
