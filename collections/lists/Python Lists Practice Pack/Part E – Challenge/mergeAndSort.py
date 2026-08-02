# Merge two lists and sort them.

wordsListOne = []
wordsListTwo = []
# Take 7 numbers
print("First list of words : ")
for i in range(3):
    word = (input(f"Enter word{i+1}: "))
    wordsListOne.append(word)

print("\nSecond list of words : ")
for i in range(3):
    word = (input(f"Enter word{i+1}: "))
    wordsListTwo.append(word)
print("\nFirst list : ",wordsListOne)
print("Second list : ",wordsListTwo)


# merge two lists
words = wordsListOne + wordsListTwo
print("\nMerging First and Second Lists : ", words)

#sorting merge lists
words.sort()
print("Sorted list : ", words)