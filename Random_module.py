print("Random Module")

import random
print("imprime entero aleatorio entre 0 y 5")
print(random.randint(0,5))

###############################

import random 
print("imprime numero de punto flotante aleatorio entre 0 y 100")
print(random.random() * 100) 

###############################

import random 
print("Elige de una lista aleatoriamente")
conan=random.choice(["Conan","Valeria","Belit"])
print(conan)

####################################

import random 
print("Elige de una lista mezclada de variables")
lst=["David",46,"Avengers",3245.32,"Pi",True,3.14,"Python"]
rnd= random.choice(lst)
print(rnd) 

#####################################

import random 
print("Baraja una lista mezclada de variables")
lst=["David",46,"Avengers",3245.32,"Pi",True,3.14,"Python"]
random.shuffle(lst)
print(lst)

#########################################

import random 
print("Crea una lista random de 0 a 20")
lista = [[i] for i in range(20)]
random.shuffle(lista)
print(lista)

##############################################

import random
print("numeros aleatorios en rango de pasos")
for i in range(10):
    print(random.randrange(0,200,7))

#############################################

import random
output= {"Heads":0, "Tails":0}
coin= list (output.keys())
print("Voltear una moneda virtual 10 mil veces")
for i in range(10000):
    output[random.choice(coin)]+=1 
print("Cara:", output["Heads"]) 
print("Cruz:",output["Tails"])   

###############################################

import random 
print("Buscador de palabras aleatorias desde un fichero de texto")
print(">>>>>>>>>>>>>>>>>>Random Word Finder<<<<<<<<<<<<<<<<<<<<<")
print("\nUsing a 466K English word text file I can pick any words at random.\n")

wds=int(input("\nHow many words shall I choose? "))

with open("./words.txt","rt") as f : 
    words=f.readlines()
words=[w.rstrip() for w in words ]
print("--------------------------")

for w in random.sample(words,wds):
    print(w)
print("--------------------------")
