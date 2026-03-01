# for loop = execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc.
#            (start, stop, step)

'''
for x in range(1, 11):
    print(x)
print("Happy Chubby Bunny!")
'''
'''
for x in reversed(range(1, 11)):
    print(x)
print("Happy Chubby Bunny!")


for x in range(1, 11, 2):
    print(x)
print("Happy Birthday Mia💃!!")

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)
'''
'''
# continue = skip the current block, and return to the "for" loop.
for x in range(1, 21):
    if x == 15:
        continue
    else:
        print(x)
'''

# break = exit / skip the "for" loop
for x in range(1, 21):
    if x == 15:
        break
    else:
        print(x)
