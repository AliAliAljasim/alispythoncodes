# This is meant to be an advanced calculator, the hopes are to be able to perform multiple functions
# This is project is completely done by Ali Ali Al-Jasim
# First is an input that makes sure that the task that is wanted is performed

# The hope is to add a delay for a bit of time to read, this is done by the import time, the code is time.sleep()
import time

print("Hey, this is Ali's Calculator")
time.sleep(1)
print("It provides some basic functions")

time.sleep(1)
print("Now its ur time to choose a function")

# A list of the functions, everytime a new function is added, add to this list so that it could be added
["Addition", "Subtraction", "Multiplication", "Division"]
print(" ")

time.sleep(2)

# This is where you determine what function you want to perform
Options=input("which option would you like to choose? ").strip().title()
match Options:
    case "Addition":
        n=1
    case "Subtraction":
        n=2
    case "Multiplication":
        n=3
    case "Division":
        n=4
    case _:
        print("Sorry that is not an available function, check your spelling")
        n="Unkown"

if n==1:
    x1=float(input("What do you want your first value to be"))
    x2=float(input("What do you want your second value to be"))
    a=2
    print(sum([x1,x2]))
