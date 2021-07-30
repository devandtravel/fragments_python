import random
import re

word_list = ["python", "java", "kotlin", "javascript"]
print("H A N G M A N\n")
random_choice = random.choice(word_list)
print("-" * len(random_choice))
possible_letters = ""
substring = ""
lives = 8
single_letter_pattern = r"^[a-z]$"
single_character_pattern = r"^.$"
multiple_letter_pattern = r"^[a-z]+$"
all_letters = ""
flag = False


def print_word():
    if substring == "":
        print("\n" + "-" * len(random_choice))
    else:
        print("\n" + re.sub(substring, "-", random_choice))


choose = input('Type "play" to play the game, "exit" to quit:')
while choose != "play" or choose != "exit":
    try:
        if choose == "play":
            while lives > 0:
                # possible letter reading
                while True:
                    possible_letter = input("Input a letter: ")
                    if possible_letter == "":
                        print("You should input a single letter\n")
                        flag = False
                        print_word()
                    if re.fullmatch(multiple_letter_pattern, possible_letter):
                        if re.fullmatch(single_letter_pattern,
                                        possible_letter):
                            flag = True
                            break
                        else:
                            print("You should input a single letter\n")
                            flag = False
                            print_word()
                    elif re.fullmatch(single_character_pattern,
                                      possible_letter):
                        print("It is not an ASCII lowercase letter")
                        flag = False
                        print_word()
                    else:
                        print("You should input a single letter")
                        flag = False
                        print_word()
                # check if input repeats
                if possible_letter in all_letters:
                    print("You already typed this letter")
                    print_word()
                    continue
                else:
                    all_letters += possible_letter
                if possible_letter in random_choice:
                    possible_letters += possible_letter
                    substring = rf"(?![{possible_letters}])."
                    if len(possible_letters) == len(random_choice):
                        print("You guessed the word!")
                        print("You survived!")
                        break
                else:
                    if flag:
                        lives -= 1
                        if lives == 0:
                            print("No such letter in the word")
                            print("You lost!")
                            break
                        else:
                            print("No such letter in the word")
                print_word()
            break
        if choose == "exit":
            break
    except ValueError:
        choose = input('Type "play" to play the game, "exit" to quit:')
