print("Formatting Strings")
print("Python 3.7.6")

name="Conan"
print ("The barbarian hero of the Hyborian Age is: {}" .format(name))

name="Conan"
place="Cimmeria"
print("{} hailed from the north, in a cold land known as {}".format(name,place))

number =10000
print("{} of {} was a skilled mercenary, and thief too. He once stole {} gold from a merchant.".format(name,place,number))


numbers= 1,3,45,567546, 3425346345
print("Some numbers: {}, {}, {}, {}, {}". format(*numbers))

numbers2=1,4,7,9
print ("More numbers: {3}, {0} , {2}, {1}".format(*numbers2))

characters = ["Conan", "Belit", "Valeria" ,19 ,27 ,20]
print ("{0} is {3} years old. Whereas {1} is  {4} years old.".format(*characters))

name = input("What's your name? ")
print("Hello {}".format(name))


name = input("What's your name? ")
print("Hello {}".format(name))
lname=list(name)
print("The first letter of your name is a {0}".format(*lname))

names = ["Conan", "Belit" , "Valeria"]
ages = [25,21,22]
print ("{0[0]} is {1[0]} years old. Whereas {0[1]} is {1[1]} years old.".format(names,ages))
