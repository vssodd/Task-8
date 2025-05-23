stalls = input('Enter a string of ten characters consisting of "a" and "b": ')
total_milk = 0
milk = 0

for stall in stalls:
    milk += 1
    if stall == 'b':
        total_milk += milk * 2

print('Total milk for the day:', total_milk, 'liters')
