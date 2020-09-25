import turtle
import numpy as np

v0=float(input("V0="))
alpha=float(input("alpha="))
k=float(input("k="))
n=float(input("n="))

dt=0.01
vy=v0*np.sin(alpha/180*np.pi)
vx=v0*np.cos(alpha/180*np.pi)
x=0
y=0

for i in range(5000):
    x+=vx*dt
    y+=vy*dt
    vy-=(10*dt+n*vy)
    vx-=n*vx
    if(y<0.01):
        vy=-k*vy
    turtle.goto(x,y)

