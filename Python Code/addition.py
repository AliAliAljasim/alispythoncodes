# int (integers) are numbers, str (string) are words, float are decimals
x= float(input("What's your first value? "))
y= float(input("What's your second value? "))

# Adds the numbers then rounds the number to the nearest integer
z= round(x + y)
print(f"{z:,}")
