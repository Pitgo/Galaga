input = str(input("Write something to check if it is a palindrome: "))
word = input.replace(" ", "")

word_len = len(word)/2
word_len = word_len.__floor__()

word_first_half = word[0:word_len].lower()
word_second_half = word[word_len:].lower()

print(word)
print(word_len)
print(word_first_half)
print(word_second_half)

if word_first_half == word_second_half[::-1]:
    print(f"{input} is a palindrome")
else:
    print(f"{input} is not a palindrome")

