print("Dictionaries")

phonebook={"Emma": 1234, "Daniel": 3456, "Hannah":6789}
phonebook2={"David": "0987 654 321"}

print phonebook
print phonebook2

print phonebook["Emma"]
print phonebook["Hannah"]

phonebook2["David"] = "0987 654 324"
del phonebook2["David"]
print phonebook2 

phonebook = {}

####################################

name = raw_input("Enter name: ")
number = int(raw_input("Enter phone number: "))
phonebook[name] = number 
print phonebook 
#print phonebook ["David"]



