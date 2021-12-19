#makes an Ice cream cone
#by bailey nichols
from turtle import *
speed(1)
x=2
y=100
f=3
while True:
   right(x)
   forward(x)
   x=x**x
   y=y+1
   if x >= 150:
       x=f
       f=f+0.1
   elif y >= 300:
       break
