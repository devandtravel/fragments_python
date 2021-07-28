number1 = input('Please enter an integer:\n> ')
while type(number1) != int:
    try:
        number1 = int(number1)
    except ValueError:
        number1 = input(
            'You have entered the wrong type of data. Enter an integer or the word "stop" to exit the program:\n> '
        )
        if number1 == 'stop':
            break
