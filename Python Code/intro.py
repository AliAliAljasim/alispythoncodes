# This is my first line of code
# Asks user for name and saves as input and removes spaces and capitals
name = input("What's your name? ").strip().title()

# About to split user's name into first name and last name
if " " in name:
    first, last = name.split(" ")
if " " in name:
    print("Hello,", first)

# Says Hello + the persons name
if not " " in name:
    print("Hello,", name)
