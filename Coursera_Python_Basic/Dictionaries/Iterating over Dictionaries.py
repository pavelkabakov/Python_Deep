inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}

for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])
print('----------')
for akey in inventory:     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])
print('----------')
ks = list(inventory.keys())       # Make a list of all of the keys
print(ks)
print(ks[0])                      # Display the first key
print('----------')
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))

for v in inventory.values():
    print("Got", v)
print('----------')
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.items()))

for k, v in inventory.items():
    print("Got", k, "that maps to", v)

"""
You may have noticed in the examples above that, to print the result of the keys(), values(), and items() methods,
 we used lines like this:

print(list(inventory.keys())
instead of this:

print(inventory.keys())
Technically, keys(), values(), and items() don’t return actual lists. Like the range function described previously,
they return objects that produce the items one at a time, rather than producing and storing all of them in advance
as a list. If you need to perform an operation on the result of one of these methods such as extracting the first
item, you must convert the result to a list using the list conversion function. For example, if you want to get
the first key, this won’t work: inventory.keys()[0]. You need to make the collection of keys into a real list
before using [0] to index into it: list(inventory.keys())[0].
"""

