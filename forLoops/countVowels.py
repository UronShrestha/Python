# count vowles and constants from a text

text = input("Enter a string : ").lower()
vowels = "aeiou"
count_vowels = 0
count_const = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            count_vowels += 1
        else:
            count_const += 1
print(f"Number of vowels in '{text}' : ", count_vowels)
print(f"Number of constants in '{text}' : ", count_const)






