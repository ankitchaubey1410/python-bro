# format specifiers = {value:flags} format a value based on what
#                              flags are inserted 

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces 
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align 
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price1 is : ${price1:.2f}")
print(f"Price2 is : ${price2:.2f}")
print(f"Price3 is : ${price3:.2f}")
# print(f"Price1 is : {price1:.3f}") #price1 = 3.141
# print(f"Price2 is : {price2:.3f}") #price2 = -987.650
# print(f"Price3 is : {price3:.3f}") #price3 = 12.340

print(f"Price1 is : ${price1:10}")   #Each value is now have 10 spaces and characters in it 
print(f"Price2 is : ${price2:10}")
print(f"Price3 is : ${price3:10}")

print(f"Price1 is : ${price1:010}")  #Each value is now have 10 spaces and each characters is filled with zero's
print(f"Price2 is : ${price2:010}") 
print(f"Price3 is : ${price3:010}")

print(f"Price1 is : ${price1:>10}")  #Each value is now have 10 spaces and each characters is filled with zero's and right justified
print(f"Price2 is : ${price2:>10}")
print(f"Price3 is : ${price3:>10}")

print(f"Price1 is : ${price1:<10}")  #Each value is now have 10 spaces and each characters is filled with zero's and left justified
print(f"Price2 is : ${price2:<10}")
print(f"Price3 is : ${price3:<10}")

print(f"Price1 is : ${price1:^10}")  #Each value is now have 10 spaces and each characters is filled with zero's and center justified
print(f"Price2 is : ${price2:^10}")
print(f"Price3 is : ${price3:^10}")

print(f"Price1 is : ${price1:+}")    #Each value shows a plus sign if it's positive and a minus sign if it's negative
print(f"Price2 is : ${price2:+}")
print(f"Price3 is : ${price3:+}")

print(f"Price1 is : ${price1: }")    #Each value shows a space in place of positive sign
print(f"Price2 is : ${price2: }")
print(f"Price3 is : ${price3: }")

print(f"Price1 is : ${price1:,}")    #Each value shows a comma separator
print(f"Price2 is : ${price2:,}")
print(f"Price3 is : ${price3:,}")

print(f"Price1 is : ${price1:+,.2f}")    #Each value shows a plus sign if it's positive and a minus sign if it's negative, rounded to 2 decimal places and with a comma separator
print(f"Price2 is : ${price2:+,.2f}")
print(f"Price3 is : ${price3:+,.2f}")