# Write a program that keeps asking the user to enter a password until they enter the correct one.
# beginner level program

correct_password = "secure123"
user_input = ""
while user_input != correct_password:
    user_input = input("Enter the password: ")
print("Access granted!")
