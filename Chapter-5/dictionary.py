# dictionary = a collection of {key: value} pairs
#              oerdered and changeable (no duplicates allowed in keys)

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
print(capitals)
print(capitals["Russia"])
capitals["Germany"] = "Berlin"
print(capitals)

print()
for key in capitals:
    print(key)
print()
for key in capitals:
    print(capitals[key])

print()
for i,j in capitals.items():
    print(f"key: {i} || value: {j}")

print()
for item in capitals.items():
    print(item)