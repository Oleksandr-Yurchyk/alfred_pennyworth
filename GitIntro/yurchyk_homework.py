from typing import List


def calculate_rooms_number(data: List[List[int]]) -> int:
    room_count = 1
    if not data:
        return room_count - 1
    else:
        for i in range(len(data)):
            if i < len(data) - 1 and data[i][1] >= data[i + 1][0]:
                room_count += 1
    return room_count
