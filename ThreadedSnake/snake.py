import curses
from curses import KEY_LEFT, KEY_DOWN, KEY_RIGHT, KEY_UP, textpad
import random
from time import sleep
from collections import namedtuple
from threading import Thread

Point = namedtuple('Point', ["y", "x"])
ARROWS = [KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_LEFT]


class Snake(list):

    def __init__(self):
        super().__init__()
        self.extend([Point(5, 5), Point(5, 6), Point(5, 7)])
        self.direction = KEY_RIGHT

    @property
    def head(self):
        return self[-1]

    def move(self, screen):
        key = screen.getch()

        if key in ARROWS:
            self.direction = key

        if self.direction == KEY_RIGHT:
            self.pop(0)
            self.append(Point(self.head.y, self.head.x + 1))

        if self.direction == KEY_LEFT:
            self.pop(0)
            self.append(Point(self.head.y, self.head.x - 1))

        if self.direction == KEY_DOWN:
            self.pop(0)
            self.append(Point(self.head.y + 1, self.head.x))

        if self.direction == KEY_UP:
            self.pop(0)
            self.append(Point(self.head.y - 1, self.head.x))


def print_snake(screen, snake):
    for point in snake[:-1]:
        screen.addch(*point, '#')
    screen.addch(snake[-1][0], snake[-1][1], '0')


def find_free_fields(snake, max_x, max_y):
    empty_field = set()
    for y in range(2, max_y - 1):
        for x in range(2, max_x - 2):
            empty_field.add(Point(y, x))
    return list(empty_field - set(snake))


# def threaded_food():
#     screen = curses.initscr()
#
#     curses.curs_set(0)  # Hides cursor
#     screen.nodelay(True)  # Allow don`t wait for user input
#     max_y, max_x = screen.getmaxyx()
#
#     snake = Snake()
#     food = random.choice(find_free_fields(snake, max_x, max_y))
#
#     while True:
#         screen.addch(*food, '*')
#         if snake.head == food:
#             snake.append(food)
#             food = random.choice(find_free_fields(snake, max_x, max_y))


def main(screen):
    screen = curses.initscr()

    curses.curs_set(0)  # Hides cursor
    screen.nodelay(True)  # Allow don`t wait for user input
    max_y, max_x = screen.getmaxyx()

    snake = Snake()
    food = random.choice(find_free_fields(snake, max_x, max_y))

    while True:
        textpad.rectangle(screen, 1, 1, max_y - 1, max_x - 2)
        snake.move(screen)
        print_snake(screen, snake)
        screen.addch(*food, '*')

        if snake.head == food:
            snake.append(food)
            food = random.choice(find_free_fields(snake, max_x, max_y))

        if snake.head.y == 1 or snake.head.y == max_y - 1 or \
                snake.head.x == 1 or snake.head.x == max_x - 2 or \
                snake.head in snake[:-2]:
            msg = 'Game over'
            screen.addstr(max_y // 2, max_x // 2 - len(msg) // 2, msg)
            screen.nodelay(False)
            screen.getch()
            break

        screen.refresh()
        sleep(0.1)
        screen.clear()


# t1 = Thread(target=main)
# t1.start()
# t1.join()
#
# t2 = Thread(target=threaded_food)
# t2.start()
# t2.join()

curses.wrapper(main)
