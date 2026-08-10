"""Adding Elements
Elements can be added to a list using the following methods:
1. append()
2. insert() 
3. extend()
"""


natural_num = [1,2,3,4,5,6]
print(natural_num)
natural_num.append(7)
print(natural_num)
print(natural_num[6])


whole_num = [0,1,2,4,5,6]
print(whole_num)
whole_num.insert(3,3)
print(whole_num)

integer = [-2, -1, 0]
print(integer)
integer.extend([1,2,3])
print(integer)