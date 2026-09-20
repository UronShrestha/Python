"""Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are 
List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.
"""

# thisSet = {"ram", "sam","dan"}
# print(thisSet)

# Duplicates not allowed
'''thisSet = {"ram", "ram", "sam", "dan"}
print(thisSet)'''


# True and 1, and False and 0 are considered the same value:
'''thisSet = {"ram", "ram", "sam", True, 1, 2, 3, False, 0, "dan"}
print(thisSet)'''

# length of a set
'''thisSet = {"ram", "ram", "sam", True, 1, 2, 3, False, 0, "dan"}
print(len(thisSet))
print(type(thisSet))
'''

# site() constructor
thisSet = set(("ram", "ram", "sam", True, 1, 2, 3, False, 0, "dan"))
print(thisSet)

