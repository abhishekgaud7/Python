Age=int(input("Enter your age:"))
print(Age)

if(Age>=18):
    print("You are eligible to vote.")
elif(Age<18):
    print("You are not eligible to vote.")
else:
    print("Invalid input.")