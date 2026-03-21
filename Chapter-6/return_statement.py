# return statements

def avg(*numbers): 
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("the average of numbers is : ", sum/len(numbers))
    return sum/len(numbers)

c = avg(1,2,3,4,5)
print(c)

