# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                    inner loop 
'''
for x in range(1, 11, 1):
    print(x, end=" ") # end = "something" -> print something at the end of the print statement instead of a new line
'''

for x in range(3):
    for y in range(1, 11):
        print(y, end="")
    print() # print a new line after the inner loop is done

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = "🥰"
for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()

for i in range(10):
    for j in range(i):
        print("👄😘💅", end=" ")
    print()