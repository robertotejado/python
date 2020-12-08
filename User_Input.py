print("User Input")
print("Python 2.7.14")
firstname=""
surname=""
print("Hello")
#For python 3 and above s = raw_input() if not input()
firstname=raw_input("What is your firstname? ")
print("Thanks.")
surname=raw_input("And what is your surname? ")
print("Thankyou Sr." + firstname + " " +surname)

print "Welcome" , firstname , surname, ". I hope you're well today"
print "Welcome" , firstname , surname + ". I hope you're well today"

print("Halt!. Who goes there?")
name= raw_input()
#print name
if name == "Robert":
    print ("Welcome, good sir. You may pass") 
else : 
    print("I know you not. Prepare for battle!")

#Code to calculate rate and distance
print("Input a rate and a distance")
rate=float(raw_input("Rate: "))
distance=float(raw_input("Distance: "))
print "Time: ", (distance / rate)