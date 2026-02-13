#Exercise 1: Rectangle Area Calc
length = float(input("Enter the length:"))
breadth = float(input("Enter the breadth:"))
area = length * breadth
print(f"Area of Rectangle is:{area} cm")

#Exercise 2: Shopping cart problem
item = input("What item would you like to buy: ")
price = float(input("What is the price of item: "))
quantity = int(input("How many would you like: "))
total = price * quantity
print(f"You have brought {quantity} X {item}s for ${total}")