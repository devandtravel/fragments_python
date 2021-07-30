import random


def hint(word, guessed_letters):
    return ''.join(
        ['-' if letter not in guessed_letters else letter for letter in word])


def hangman():
    secret_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
    guessed_letters = set()
    previous_letters = set()
    number_errors_made = 0

    while number_errors_made < 8:
        print()
        print(hint(secret_word, guessed_letters))

        guess = input('Input a letter: ')

        # Guard conditions
        if guess in previous_letters:
            print('You already typed this letter')
            continue
        if not len(guess) == 1:
            print('You should input a single letter')
            continue
        if not guess.isascii() or not guess.islower():
            print('It is not an ASCII lowercase letter')
            continue

        previous_letters.add(guess)

        if guess not in secret_word:
            print('No such letter in the word')
            number_errors_made += 1
        else:
            guessed_letters.add(guess)

        if guessed_letters == set(secret_word):
            print('You guessed the word')
            print('You survived!')
            break

        if number_errors_made == 8:
            print('You are hanged!')
            break


random.seed()

print('H A N G M A N')

while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        hangman()
    elif choice == 'exit':
        break
