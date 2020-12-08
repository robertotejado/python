print("Splitting and Joining Strings")

text= "Daniel Hannah Emma" 
names = text.split(" ")
print ("Split")
print (names)

#########################################

texto="January,February,March,April,May,June"
months= texto.split(",")
print ("Split")
print (months)

################################

name= list("David")
print ("List")
print  (name)

#####################################

alphabet = "".join(["a","b","c","d","e"])
print ("Join")
print (alphabet)
###########################################

name="".join(name)
print ("Join")
print (name)

###########################################

Lista=["Conan", "raised", "his", "mighty", "sword","and", "struck", "the", "demon" ]
text=" ".join(Lista)
print ("Join")
print(text)

###############################################

colours= ["Red","Green","Blue"]
col= ",".join(colours)
print ("Join")
print(col)

############################################

title="conan the cimmerian"
title.capitalize()
print("Capitalizar")
print(title.title())

############################################

message="Have a nice day"
print("logic operators on strings")
print ("nice" in message)
print("bad" not in message)
print("day" not in message)
print("night" in message)
