print("Writing to files")

t = open("./text.txt","w")
t.write("You awake in a small, square room. A Single table stands to one side, there is a Locked door in front of you.")
t.close()


t2 = open("./text2.txt","a")
t2.write("\n")
t2.write("You stand and survey your surroundings.On top of the table is some meat, and a cup of water. \n")
t2.write("The door is made of solid oak with iron strips. It's bolted from the outside, locking you in. You are a prisioner! \n")
t2.close() 

import math 
print("Value of Pi is: ",math.pi)
print("\nWriting to a file now...")
pi= math.pi
t= open("./pi.txt","w")
t.write("Value of Pi is: {}".format(pi))
t.close()
