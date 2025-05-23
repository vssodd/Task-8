word = input("Enter a string: ")
if word == word[::-1]:
    print('Yes. It is a palindrome!')
else:
    print('No. It is not a palindrome!')
