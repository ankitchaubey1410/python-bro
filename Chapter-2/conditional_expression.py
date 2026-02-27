# conditional expression = A one-line shortcut of the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition             
#                          X if condition else Y

num = 5
a = 6
b = 7
age = 15
temperature = 20
user_role = "admin"

# print("Positive" if num > 0 else "Negative")

# result = "EVEN" if num % 2 == 0 else "ODD"
# print(result)

# max_num = a if a > b else b
# print(max_num) 
# min_num = a if b > a else b
# print(min_num)

# status = "ADULT" if age >= 18 else "CHILD"
# print(status)

# weather = "HOT🥵" if temperature > 20 else "COLD🥶"
# print(weather)

access_level = "FULL ACCESS" if user_role == "admin" else "LIMITED ACCESS"
print(access_level)