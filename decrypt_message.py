word = input('Enter the encrypted message: ')
first = ''
second = ''
counter = 0

for char in word:
    counter += 1
    if counter % 2 == 0:
        second = char + second
    else:
        first += char

print(first + second)
