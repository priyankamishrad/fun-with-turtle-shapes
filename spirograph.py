import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  return (r, g, b)

for _ in range(int(360/10)):
  tim.color(random_color())
  tim.circle(50)
  tim.tilt(10)
  tim.left(10)


