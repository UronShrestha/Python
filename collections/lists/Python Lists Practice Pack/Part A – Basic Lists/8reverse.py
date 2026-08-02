# Print the list in reverse order using indexing

num = [1,2,3,4,5]
for i in range(len(num)-1,-1,-1):
    print(num[i])

'''
# using negative-step slicing.
num = [1,2,3,4,5]
print(num[::-1])
'''

'''
# using reverse() method
num.reverse()
print(num)
'''