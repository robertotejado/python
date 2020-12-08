print("Lists")
print("Python 2.7.14")

numbers = [1, 4, 7, 21, 98, 156]
mythical_creatures = ["Unicorn", "Balrog","Vampire", "Dragon", "Minotaur"]

print numbers
print numbers[0]

print mythical_creatures
print mythical_creatures[0]
print mythical_creatures[3]

# menos- Desde los ultimos
print mythical_creatures[-1]
print mythical_creatures[-4]


print (numbers[1:3])
print (numbers[0:4])
print (numbers[3:5])
print (numbers[1:])

#################################

everything = numbers + mythical_creatures
print(everything)

numbers=numbers+[201] #inserta numero

mythical_creatures = mythical_creatures+["Griffin"] #inserta Nombre
mythical_creatures.append("Nessie") #inserta nombre
numbers.append(278) #inserta numero


del numbers[7] #Elimina el espacio del 7 que es el 278
mythical_creatures.remove("Nessie") #Elimina el nombre de Nessie


numbers.insert (4, 62)
numbers.pop(4)

print(mythical_creatures)
print(numbers)

#########################################


print(list("David"))
name = list("David Hayward")
print name
age=[44]
user = name + age 
print user

#######################################

name = raw_input ("What's your name?")
lname = list(name)
age = int (raw_input("How old are you: "))
lage = [age] 
user = lname + lage
print(user) 
