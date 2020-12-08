print("Tuples")
print("Python 2.7.14")

months=("January", "February", "March", "April", "May" , "June" )
#print months

print months[0]
print months[5]

print months

NPC =[ ("Conan",100) , ("Belit",80) ,("Valeria",95)]
print NPC
print NPC[0][0]
print NPC[0][1]
print NPC[1][0]
print NPC[1][1]
print NPC[2][0]
print NPC[2][1]

#############################

NPC2 = ("Conan",100)
(name,combat_rating) = NPC2 #desempaqueta tupla en dos variables
print name 
print combat_rating

############################


NPC3 =[ ("Conan",100) , ("Belit",80) ,("Valeria",95)]
print NPC3 [2][-0]

#################################

numbers=(10.3, 23, 45.2, 109.3, 6.1, 56.7, 99)
print("Numero maximo de tupla")
print (max(numbers))
print("Numero minimo de tupla")
print (min(numbers))