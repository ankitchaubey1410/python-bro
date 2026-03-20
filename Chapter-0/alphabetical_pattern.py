x = int(input("enter a number : "))
# print(ord('a'))
# it is used to find ascii value of that character
# print(chr(65))
# it is used to check what character is in that ascii value


for i in range(0,x,1):
    for j in range(0,x,1):
        print(chr(i+65),end=" ")
    print()

print()
print()

for i in range(0,x,1):
    for j in range(0,x,1):
        print(chr(j+65),end=" ")
    print()

print()
print()

for i in range(0,x,1):
    for j in range(0,i+1,1):
        print(chr(j+65),end=" ")
    print()

print()
print()

for i in range(0,x,1):
    for j in range(0,i+1,1):
        print(chr(i+65),end=" ")
    print()

print()
print()

num = 65
for i in range(0,x,1):
    for j in range(0,i+1,1):
        print(chr(num),end=" ")
        num += 1
    print()

print()
print()

num = 65
for i in range(0,x,1):
    for j in range(0,x,1):
        print(chr(num),end=" ")
        num += 1
    print()