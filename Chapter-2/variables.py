# Variables =  A for a value (string, integer, float, boolean)
#              A variable behaves as if it was the value it contains


#Strings is a series of characters. They can include numbers but we treat them as characters
first_name = "Bro"
food = "pizza"
email = "ankitchaubey1421@gmail.com"

#print(first_name)

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")

#Integers is a whole number
age = 25
quantity = 3
num_of_students = 30
print(f"You are {age} years old!")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#Floats means floating point numbers or decimal numbers
price = 10.99
gpa = 7.8
distance = 4.4
print(f"The price is {price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance} km")

#Boolean True or False
is_student = True
for_sale = False
print(f"Are you a student {is_student}")
print("Boolean value for student = ",int(is_student))

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("This item is for sale!")
else:
    print("This item is not for sale!")