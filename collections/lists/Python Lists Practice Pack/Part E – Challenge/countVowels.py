# Count vowels inside a list of words.

words = []

# Take 7 numbers
for i in range(3):
    word = (input(f"Enter word{i+1}: "))
    words.append(word)
print(words)

vowels = "aeiou"
count = 0

for word in words:
    for letter in word:
        if letter.lower() in vowels:
            count += 1
print("Vowles count : ", count)
