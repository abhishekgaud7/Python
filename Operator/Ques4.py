# logical Operators in Python are used to combine conditional statements.
#  The three main logical operators are:
# and, or, and not.

c =True
d =False

print("c and d :", c and d)  # Returns True if both statements are true
print("c or d :", c or d)    # Returns True if one of the statements is true
print("not c :", not c)       # Reverse the result, returns False if the result is true
print("not d :", not d)       # Reverse the result, returns True if the result is false

# Example with numbers
x = 5
y = 10
print(" (x > 2) and (y < 15) :", (x > 2) and (y < 15))  # True and True -> True
print(" (x > 2) or (y > 15)  :", (x > 2) or (y > 15))   # True or False -> True
print(" not (x > 2)          :", not (x > 2))            # not True -> False
print(" not (y < 15)         :", not (y < 15))           # not True -> False
