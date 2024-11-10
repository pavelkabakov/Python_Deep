"""
Looking up a value in a dictionary is a potentially dangerous operation. When using the [] operator to access a key,
 if the key is not present, a runtime error occurs. There are two ways to deal with this problem.

The first approach is to use the in and not in operators, which can test if a key is in the dictionary:
"""

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")
print("-------------------------------------")
"""
The second approach is to use the get method. get retrieves the value associated with a key, similar to the [] operator. 
The important difference is that get will not cause a runtime error if the key is not present. It will instead return 
the value None. There exists a variation of get that allows a second parameter that serves as an alternative return value 
in the case where the key is not present. This can be seen in the final example below. In this case, since “cherries”
 is not a key, get returns 0 (instead of None).
"""

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries",0))