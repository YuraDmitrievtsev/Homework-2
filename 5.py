import turtle
import numpy as np
from random import randint
from numpy import abs


def r(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


turtle.penup()
n = 400
turtle.goto(n, n)
turtle.pendown()
turtle.goto(n, -n)
turtle.goto(-n, -n)
turtle.goto(-n, n)
turtle.goto(n, n)

number_of_turtles = 40
steps_of_time_number = 100
pool = [turtle.Turtle(shape= 'circle') for i in range(number_of_turtles)]
X = []
Y = []
Vx = []
Vy = []
N = 0
for unit in pool:
    N += 1
    unit.penup()
    Vx.append(randint(-500, 500)*1)
    Vy.append(randint(-500, 500)*1)
    unit.speed(np.sqrt(Vx[N - 1] ** 2 + Vy[N - 1] ** 2))
    X.append(randint(-n, n))
    Y.append(randint(-n, n))
    unit.goto(X[N - 1], Y[N - 1])

m = 1
dt = 0.01
eps = 10
sig = 1
for infinity in range(50000):
    print(infinity)
    Fx = [0] * N
    Fy = [0] * N
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            R = r(X[i], Y[i], X[j], Y[j])
            Fx[i] += 8 * eps * sig * (2 * (sig / R) ** 11 - (sig / R) ** 5) * (X[j] - X[i]) / R
            Fx[j] += 8 * eps * sig * (2 * (sig / R) ** 11 - (sig / R) ** 5) * (X[i] - X[j]) / R
            Fy[i] += 8 * eps * sig * (2 * (sig / R) ** 11 - (sig / R) ** 5) * (Y[j] - Y[i]) / R
            Fy[j] += 8 * eps * sig * (2 * (sig / R) ** 11 - (sig / R) ** 5) * (Y[i] - Y[j]) / R
    for i in range(N):
        X[i] += Vx[i] * dt
        Y[i] += Vy[i] * dt
        pool[i].goto(X[i],Y[i])
        Vx[i] += Fx[i] / m * dt
        Vy[i] += Fy[i] / m * dt
        if not(abs(X[i]) < n):
        #if abs(X[i] - n) < 0.01 or abs(X[i] + n) < 0.01:
            Vx[i] *= (-1)
        if not(abs(Y[i]) < n): #abs(Y[i] - n) < 0.01 or abs(Y[i] + n) < 0.01:
            Vy[i] *= (-1)
input()
