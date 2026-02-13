#Typecasting = the process of converting a variable from one data type to another
#              str(), int(), float(), bool() 

name = "Bro Code"
age = 25
gpa = 3.2
is_student = True 
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(f"GPA = {gpa}")
print(type(gpa))

name = bool(name)
print(name)

name = ""
name = bool(name)
print(name)