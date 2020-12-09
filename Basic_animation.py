from tkinter import * 
import time 

print("Basic Animation")

gui =Tk()
gui.geometry("800x600")
gui.title("Pi Animation")

canvas = Canvas(gui, width=800,height=600,bg='white')
canvas.pack()

ball1=canvas.create_oval(5,5,60,60,fill='red')
'''
a = 5 
b = 5 

for x in range (1,100):
        canvas.move(ball1,a,b)
        gui.update()
        time.sleep(.01)
'''

##Animating the ball
xa = 5 
ya = 5 
while True: 
    canvas.move(ball1,xa,ya)
    pos=canvas.coords(ball1)
    if pos[3] >=600 or pos[1] <=0:
        ya = -ya  
    if pos[2] >= 800 or  pos[0] <=0:
        xa = -xa
    gui.update()
    time.sleep(.025)

gui.mainloop()