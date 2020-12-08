print("Opening Files")

import time
poem= open("./poem.txt")
print(poem)
#print("Lee el texto completo")
#print(poem.read())

#print("Lee los 10 primeros caracteres")
#print(poem.read(10))

#print("Lee una linea de texto")
#print(poem.readline())

#print("Lee una linea de texto")
#line= poem.readline()
#print(line)

###############################
#print("Lee todas las lineas y las almacena en listas")
#lines= poem.readlines()
#print(lines[0])
#print(lines[1])
#print(lines[2])

########################################

#for lines in lines :
#    print(lines)

########################################


#for lines in poem: 
#    print(lines)

#######################################

lines = poem.read()
for lines in lines:
    print(lines, end="")
    time.sleep(.15)
    

