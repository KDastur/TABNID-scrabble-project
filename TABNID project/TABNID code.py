from itertools import permutations

letters = "tabind"

# Load the dictionary
with open("dictionary.txt", "r") as f:
    words = [word.strip().lower() for word in f]

# Check each word
results = []
for word in words:
    if all(word.count(letter) <= letters.count(letter) for letter in word):
        results.append(word)

# Sort and print
results.sort()
for word in results:
    print(word)
