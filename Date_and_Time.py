print("Date and Time")
print("Python 3.7.6")
import time
time.asctime()

print("Imprime tiempo local")
print(time.localtime())
print("Dia de la semana")
print(time.strftime('%A'))
print("Dia de la semana corto")
print(time.strftime("%a"))
print("Mes")
print(time.strftime("%B"))
print("Mes corto")
print(time.strftime("%b"))
print("Hora")
print(time.strftime("%H"))
print("hora y minuto")
print(time.strftime("%H:%M"))

##################################

import time
name=input("Enter Login name: ")
print("Welcome", name, " ")
print("User:", name, "Logged in at", time.strftime("%H:%M"))

##############################################

import time

start_time = time.time()
name=input("Enter login name:")
endtime= time.time()-start_time
print("\nWelcome", name)
print("User:", name, "Logged in at", time.strftime("%H:%M"))
print("It took", name, endtime, "seconds to login to their account.")


print("Help for time")
print(help(time))



