x = int(input("enter a number : "))

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
