print("Hello , Guys")

age = 21
print("Your age is : ",age) 
print(type(age))

cgpa = 7.5
print("Your CGPA is : ",cgpa)       
print(type(cgpa))

name = "Abhishek"
print("Your name is : ",name)
print(type(name))

is_completed = True
print("Is the course completed ? : ",is_completed)
print(type(is_completed))

print("\n\n")
# Now , I will do the same thing but by taking input from the user
age = int(input("Enter your age : "))
print("Your age is : ",age)
print(type(age))

cgpa = float(input("Enter your CGPA : "))
print("Your CGPA is : ",cgpa)
print(type(cgpa))
name = input("Enter your name : ")
print("Your name is : ",name)
print(type(name))
is_completed = input("Is the course completed ? (True/False) : ")
if is_completed == "True":
    is_completed = True
else:
    is_completed = False
print("Is the course completed ? : ",is_completed)
print(type(is_completed))
