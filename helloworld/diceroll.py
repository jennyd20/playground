
#import numpy as np
import random


#Print a random value
""" 
msg = "Roll a die, now!"
print(msg)

for i in range(1,20):
    print(random.randrange(1, 9))

 """
#print(np.random.randint(1,9))

#############################################################

#Take user input for size of die to roll

""" def dieroll(d):
    print("Rolling a " + str(d) + " sided die...")
    print (random.randrange(1, d))

value = False

while value is False:
    size = input("What size die would you like to roll?  ")
    try:
        size = int(size)
    except:
        print("Try again, silly.  Give me a number.  ")
    else:
        value = True
        dieroll(size) """


##############################################################

# Take user input for die roll, chide them after n attempts if they are being snarky

""" num_retries = 3

def dieroll(d):
    print("Rolling a " + str(d) + " sided die...")
    print (random.randrange(1, d))

size = input("What size die would you like to roll?  ")

for x in range(0, num_retries):
    try:
        i = int(size)
    except:
        if (x < num_retries - 2):
            size = input("Try again, silly.  Give me a number.  ")
        elif (x == num_retries - 2):
            size = input("This is your last try to put in a valid integer.  You can do it!  ")
        else:
            print("\nI am so disappointed in you right now.")
            break

    else:
        dieroll(i)
        break """



##############################################################

# Take user input for die roll, chide them after n attempts if they are being snarky.  Also yell at them for numbers less than 2
num_tries = 5

def dieroll(d):
    print("Rolling a " + str(d) + " sided die...")
    print (random.randrange(1, d))

size = input("What size die would you like to roll?  ")

for x in range(0, num_tries):
    try:
        i = int(size)
        if (i < 2):
            print("I can't roll a die of size " + size + "!")
            raise
    except:
        if (x < num_tries - 2):
            size = input("Try again, silly.  Give me a number.  ")
        elif (x == num_tries - 2):
            size = input("This is your last try to put in a valid integer.  You can do it!  ")
        else:
            print("\nI am so disappointed in you right now.")
            break

    else:
        dieroll(i)
        break