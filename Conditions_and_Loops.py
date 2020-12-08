print("Conditions and Loops")

word = raw_input("Please enter a four-letter word: ")
word_lenght= len(word) 

if word_lenght == 4 : 
    print word, "is a four-letter word. Well done."
elif word_lenght == 3 :
    print word, "is a three-letter word. Try again."
else: 
    print word , "is not a four-letter word."


x=1 
while x < 10:
    print(x)
    x=x+1
 # print 1 2 3 4 5 6 7 8 9


words=["Cat","Dog","Unicorn"]

for word in words:
    print(word)
    #print Cat Dog Unicorn

for x in range (1 , 10): 
    print(x)
 # print 1 2 3 4 5 6 7 8 9
