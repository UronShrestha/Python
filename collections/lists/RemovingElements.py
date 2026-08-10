"""Removing Elements
Elements can be removed from a list using the following methods:
1. remove()
2. pop()
3. del statement
4. clear()
"""

fruits = ["apple", "banana", "mango", "citrus", "kiwi"]
fruits.remove("banana")
print(fruits)

name = ["ram", "sam", "dan", "han", "gan"]
name.pop(0)
print(name)

sub = ["math", "science", "social", "english"]
del sub[0]
print(sub)

district = ["palpa", "rolpa", "gulmi"]
print(district)
del district
# print(district)

brand = ["apple", "windows", "lg"]
brand.clear()
print(brand)