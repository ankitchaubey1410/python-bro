# User defined function

def CalculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if (a>b):
        print("first number is greater!!")
    else:
        print("second number is greater or equal!!")

def isLesser(a, b):
    pass

a = 9
b = 8
CalculateGmean(a, b)
isGreater(a, b)
c = 5
d = 6
CalculateGmean(c, d)
isGreater(c, d)

# Build in functions : min() , max() , sum() , len() , type() , range() , dict() , list() , tuple() , set() , print() ...etc.

str = "ANKIT CHAUBEY"
l = list(str)
print(l)
t = tuple(str)
print(t)
s = set(str)
print(s)

for i in t:
    print(i,end=" ")