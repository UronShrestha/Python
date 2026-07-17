"""Internal Representation of Lists
Python list stores references to objects, not the actual values directly.

The list keeps memory addresses of objects like integers, strings or booleans.
Actual objects exist separately in memory.
Modifying a mutable object inside a list changes the original object.
Reassigning an immutable object creates a new object instead of changing the old one."""

a = [1,2,4]
print(a[1])
print(a)

string = list((1000,"Ram", 302, "Dam"))
print(string[0])
print(string)