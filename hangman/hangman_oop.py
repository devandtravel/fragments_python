from random import choice
from random import seed


class Hangman:

    """ Initialization """
    def __init__(self):
        self.words_list = ['python', 'java', 'kotlin', 'javascript']
        self.word = None  # Secret word
        self.mask = None  # Mask state now
        self.contaner = set()  # Letters was tried
        self.attempts = 8
        self.menu = {'play': self.start, 'exit': self.game_exit}  # menu items

    @staticmethod
    def print_title():
        print('H A N G M A N')

    """ Show menu and execute function from menu item selected (PLAY / EXIT) """
    def show_menu(self):
        menuitem = input('Type "play" to play the game, "exit" to quit: ')
        while menuitem not in self.menu:
            menuitem = input('Type "play" to play the game, "exit" to quit: ')
        print()
        self.menu[menuitem]()  # Execute function from menu item selected

    """ Get choice and set mask length """
    def set_word(self):
        seed()
        self.word = choice(self.words_list)
        self.mask = ['-' for i in range(len(self.word))]

    """ Print mask state """
    def print_mask(self):
        print(*self.mask, sep='')

    """ Check userdata for requirements of input """
    def check_input(self):
        text = input('Input a letter: ')
        if len(text) == 1:  # Checking userdata length
            if (not (text.isascii())) or (not text.islower()):  # Checking userdata for ASCII lowercase
                print("It is not an ASCII lowercase letter\n")
                self.print_mask()
                return self.check_input()
            elif text in self.contaner:  # Checking if tried to input letter again
                print("You already typed this letter\n")
                self.print_mask()
                return self.check_input()
            else:
                return text  # Return correct userdata (ASCII lowercase letter)
        else:
            print("You should input a single letter\n")
            self.print_mask()
            return self.check_input()

    """ Membership check for letter in secret word """
    def try_input(self):
        self.print_mask()
        letter = self.check_input()
        if letter in self.word:
            if letter not in self.contaner:
                for i in range(len(self.word)):
                    if self.word[i] == letter:
                        self.mask[i] = letter
                if '-' in self.mask:
                    print()
            else:
                self.attempts -= 1  # Reduce attempts if letter is in secret word, but already was input
        else:
            self.attempts -= 1  # Reduce attempts if letter is not in secret word
            print("No such letter in the word" if self.attempts < 1 else "No such letter in the word\n")
        self.contaner.add(letter)

    """ Start and play """
    def start(self):
        self.set_word()
        while self.attempts > 0:
            self.try_input()
            if set(self.mask) == set(self.word):
                print(f"You guessed the word {self.word}!\nYou survived!\n")  # If win
                self.show_menu()
                return
        print('You are hanged!\n')  # if lose
        # Game over!
        self.show_menu()

    @staticmethod
    def game_exit():  # Exit
        exit(0)


""" Game initialization and start process """
game = Hangman()
game.print_title()
game.show_menu()
