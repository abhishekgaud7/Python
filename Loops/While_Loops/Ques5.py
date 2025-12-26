# Use a while loop to reverse a given number (e.g., 123 → 321).

number = int(input("Enter a number to reverse: "))
reversed_number = 0 
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
print("Reversed Number:", reversed_number)
