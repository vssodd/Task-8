x, y = 8, 10

while True:
    print('Rover is at position', x, y, 'Enter command:')
    command = input()
    if command == 'W':
        y = min(y + 1, 20)
    elif command == 'S':
        y = max(y - 1, 0)
    elif command == 'A':
        x = max(x - 1, 0)
    elif command == 'D':
        x = min(x + 1, 15)
