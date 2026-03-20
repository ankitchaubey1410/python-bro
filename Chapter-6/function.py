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