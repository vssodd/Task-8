text = input('Enter text: ')
position = 0
index = 1
for symbol in text:
    if symbol == '*':
        position = index
        break
    index += 1
print('The symbol "*" is at position', position)
