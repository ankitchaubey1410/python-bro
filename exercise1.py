#Calc Circumference of a circle
'''
import math
radius = float(input("Enter the radius of the circle:"))

circumference = 2 * math.pi * radius

# print(f"The circumference is: {circumference}")
print(f"The circumference is: {round(circumference,2)}")

'''
#Calc Area of the circle
'''
import math
radius = float(input("Enter the radius of the circle:"))
area = math.pi * pow(radius, 2)
print(f"The area is: {round(area, 2)}")
'''

#Calc Hypotenuse of a triangle
import math
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2)+pow(b, 2))
print(f"side C: {c}")