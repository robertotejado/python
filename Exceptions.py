print("Exceptions")

try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print(a/b)
except ZeroDivisionError:
    print("You have tried to divide by zero!")
else:    
    print("You didn't divide by zero.Well done!")
#######################################################################

try:
    txt = open("./textfile.txt","r") ##To fix change to a w here
    txt.write("This is a test. Normal service will shortly resume!")
except IOError:
    print("Error: unable to write the file. Check permissions")
else:
    print("Content written to file successfully. Have a nice day.")
    txt.close()

#########################################################

try:
    txt = open("./textfile.txt" , "r")
    try:
        txt.write("This is a test. Normal service will shortly resume!")
    finally:
        print("Content written to a file successfully. Have a nice day.")
        txt.close()
except IOError:
    print("Error: unable to write the file. Check permissions")



    