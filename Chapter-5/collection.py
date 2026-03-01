# collection = single "variable" used to store multiple values
#   List  = [] oredered and changeable. Duplicates OK
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER than List
#   Set   = {} unordered and immutable, but Add / Remove OK. No Duplicates

List = [1, 2, 3, 4, 5]
Tuple = (1, 2, 3, 4, 5)
Set = {1, 2, 3, 4, 5}
datatypes = [List, Tuple, Set]
print(datatypes)
for data in datatypes:
    print(f"{data} type: {type(data)}")