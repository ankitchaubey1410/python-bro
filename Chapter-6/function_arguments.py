# function arguments

def average(a=9, b=1): # default arguments
    print("the average is : ", ((a+b)/2))

average(4, 6)
average(5)
average(b=9)

average(b=9, a=21)

def name(fname, mname, lname): # keyword arguments
    print("Hello,", fname, mname, lname)

name(mname = "Debbie", lname = "Becky", fname = "Jenna")

def sum(x, y, z=10):
    print("sum of two numbers : ", (x+y+z))

sum(99, 1) # required arguments  
sum(x=1,y=2,z=3)

def avg(*numbers): # this *numbers is now tuple which stores numbers
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("the average of numbers is : ", sum/len(numbers))

avg(1,2,3,4,5) # variable length argument

def name(*name): # arbitrary arguments
    print("Hello,", name[0], name[1], name[2])

name("Jacy", "Beth", "Brownie")


def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Jerry", lname = "Sophia", fname = "Rachel")