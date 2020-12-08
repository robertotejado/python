print("Variables")
print("Python 2.7.14")
name="David Hayward"
print name 
print type (name) 
title="Descended from Celts"
print name + ": " +title 
character = name + ": "+ title
print character 
age = 44
print type (age)

# error cant concatenate print (name +  age) 

print (character + " is " + str(age) + " years old.")
print character, "is", age, "years old."
 
age= input ("How  old are you? ")
print type(age)

age= age + 10
# error int!  str(age) + 10 
print age

shirt=19.99
print type(shirt)
print int(shirt) #el cast a int redondea a la baja

