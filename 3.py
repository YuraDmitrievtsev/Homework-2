from random import *
import turtle

inp = open('input.txt', 'r')
NUM=[]
for i in range(10):
    A = list(map(int, inp.readline().split()))
    B = list(map(int, inp.readline().split()))
    NUM.append([A,B])
    c = list(map(int, inp.readline().split()))


def draw_number(tmp_num, i):
    kx = tmp_num[0]
    ky = tmp_num[1]
    turtle.penup()
    x = i * 50
    y = 0
    turtle.goto(x, y)
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
