from random import *
import turtle

X = 0
Y = 0

NUM = []
NUM.append(((-1, 0, 1, 0), (0, -2, 0, 2)))  # 0
NUM.append(((-1, 1, 0, 0), (-1, 1, -2, 2)))  # 1
NUM.append(((-1, 1, 0, -1, 1, -1, 1, 0), (0, 0, -1, -1, 0, 0, 1, 1)))  # 2
NUM.append(((-1, 1, -1, 1, -1, 1, -1, 1), (0, 0, -1, 0, -1, 1, 0, 1)))  # 3
NUM.append(((0, 0, -1, 0, 0, 1, 0), (-2, 1, 0, 1, -1, 0, 1)))  # 4
NUM.append(((-1, 0, 1, 0, -1, 1, 0, -1, 0, 1), (0, -1, 0, -1, 0, 0, 1, 0, 1, 0)))  # 5
NUM.append(((-1, 0, 1, 0, -1, 1), (-1, -1, 0, 1, 0, 1)))  # 6
NUM.append(((-1, 1, -1, 0, 0, 1), (0, 0, -1, -1, 1, 1)))  # 7
NUM.append(((-1, 0, 1, 0, -1, 1, 0), (0, -2, 0, 1, 0, 0, 1)))  # 8
NUM.append(((-1, 0, 1, -1, 1, 0), (0, -1, 0, -1, 1, 1)))  # 9


def draw_number(tmp_num, i):
    kx = tmp_num[0]
    ky = tmp_num[1]
    turtle.penup()
    x = i * 50
    y = 0
    turtle.goto(x, y)
    print(kx, ky, len(kx))
    turtle.pendown()
    for j in range(len(kx)):
        x += kx[j] * 25
        y += ky[j] * 25
        turtle.goto(x, y)
    turtle.penup()


n = input()
for i in range(len(n)):
    draw_number(NUM[int(n[i])], i)

turtle.goto(10000, 10000)
for i in range(500):
    turtle.left(randint(0, 360))
    turtle.forward(randint(1, 50))
input()
