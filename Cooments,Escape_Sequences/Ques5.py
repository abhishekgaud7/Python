# Here’s a clear and runnable Python example showing how the sep and end parameters work in the print() function.
# Python# Demonstrating sep and end in Python's print()

# Example 1: Default behavior
print("apple", "banana", "cherry")
# Output: apple banana cherry  (default sep=' ', end='\n')

# Example 2: Using sep to change the separator between values
print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry

print("2025", "12", "21", sep="-")
# Output: 2025-12-21

# Example 3: Using end to change what is printed at the end
print("Hello", end=" ")
print("World!")
# Output: Hello World!  (no newline between prints)

print("Loading", end="...")
print("Done")
# Output: Loading...Done

# Example 4: Combining sep and end
print("Python", "Java", "C++", sep=" | ", end=" <-- End of List\n")
# Output: Python | Java | C++ <-- End of List

# Key Points:

# sep (separator) → Defines what goes between multiple arguments in print().
# Default: " " (space).
# end → Defines what is printed after the output.
# Default: "\n" (newline).

# If you want, I can also give you a visual diagram showing how sep and end affect the output flow.
# Do you want me to prepare that?
