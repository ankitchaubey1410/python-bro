# Countdown Timer Program

import time
'''
time.sleep(10) # sleep function pauses the program for that gien amount of time in seconds inside parentheses
print("TIME'S UP!!")
'''
'''
my_time = int(input("Enter the time in seconds: "))
# for x in reversed(range(0, my_time)):
for x in range(my_time, 0, -1):
    print("TIME LEFT: ", x)
    time.sleep(1)
print("TIME'S UP!!")
'''

my_time = int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int((x / 60) % 60)
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP!!")