from turtle import Turtle, Screen
import random

t = Turtle()
t.shape('arrow')

colors = ['purple2','VioletRed4','magenta','orchid','snow4','red2','RosyBrown','LimeGreen','turquoise','tan']


for i in range(3,11):
  angle = 360 / i
  t.color(random.choice(colors))
  for _ in range(i):
    t.forward(100)
    t.right(angle)
    t.forward(10)
    


screen = Screen()
screen.exitonclick()
