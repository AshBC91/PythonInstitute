word_without_vowels = ""

user_word = input("Type a word: ")
user_word = user_word.upper()
vowels = "AEIOU"

for letter in user_word:
    if letter in vowels: continue
    word_without_vowels += letter

print(word_without_vowels)

