rows = int(input('Enter the number of rows: '))
seats = int(input('Enter the number of seats per row: '))
meters = int(input('Enter the number of meters between rows: '))

for _ in range(rows):
    print('=' * seats, '*' * meters, '=' * seats, end='')
