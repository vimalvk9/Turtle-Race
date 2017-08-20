#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140,140)

for step in range(15):
  write(step,align = 'center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
  
lucky = Turtle()
lucky.color('green')
lucky.shape('turtle')
lucky.penup()
lucky.goto(-160,100)
for x in range(10):
  lucky.right(36)
lucky.pendown()

vimal = Turtle()
vimal.color('blue')
vimal.shape('turtle')
vimal.penup()
vimal.goto(-160,60)
for x in range(10):
  vimal.right(36)
vimal.pendown()


for turn in range(100):
 lucky.forward(randint(1,5))
 vimal.forward(randint(1,5))












