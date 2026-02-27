# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True   
#                     and = both conditions must be True
#                     not = inverts the condition (not True, not False)      

'''
temp = 20
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
'''

temp = 28
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside🥵")
    print("It is SUNNY☀️")

elif temp <= 0 and is_sunny:
    print("It is COLD outside🥶")
    print("It is SUNNY☀️")

# elif temp > 28 and temp < 0 and is_sunny:
elif 28 > temp> 0 and is_sunny:                        #EFFECTIVE WAY
    print("It is WARM outside😊")
    print("It is SUNNY☀️")

elif temp >= 28 and not is_sunny:
    print("It is HOT outside🥵")
    print("It is CLOUDY🌧️")

elif temp <= 0 and not is_sunny:
    print("It is COLD outside🥶")
    print("It is CLOUDY🌧️")

elif 28 > temp> 0 and is_sunny:
    print("It is WARM outside😊")
    print("It is CLOUDY🌧️")
