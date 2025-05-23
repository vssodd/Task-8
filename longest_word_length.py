text = input("Enter text: ")
current_word = ''
max_length = 0

for char in text:
    if char != ' ':
        current_word += char
    else:
        word_length = len(current_word)
        if word_length > max_length:
            max_length = word_length
        current_word = ''

# Check the last word after the loop ends
word_length = len(current_word)
if word_length > max_length:
    max_length = word_length

print('The longest word length:', max_length)
