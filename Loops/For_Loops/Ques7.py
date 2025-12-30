# Make a Marraige invitation list program
# The program should ask the user to enter names one by one.
# The user can type 'done' when they have finished entering names.
# After that, the program should print the total number of invitations sent
# and list all the names that were invited.
invited_names = []
while True:
    name = input("Enter a name to invite (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    invited_names.append(name)
print(f"\nTotal invitations sent: {len(invited_names)}")
print("Invited Names:")
for name in invited_names:
    print(name)