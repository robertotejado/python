print("Python Graphics")
print("python3")
import turtle
#turtle.circle(50)
#print(turtle.getscreen()._root.mainloop())
################################################
#turtle.circle(50,180)
#print(turtle.getscreen()._root.mainloop())
###########################################################
#print("Drawing a square ...")
#turtle.color("Red","Yellow")
#turtle.shape("turtle")
#turtle.begin_fill()
#for t in range(4):
#    turtle.forward(100)
#    turtle.left(90)
#turtle.end_fill()
#print(turtle.getscreen()._root.mainloop())

#######################################################

from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) <1:
        break
end_fill()
done()


