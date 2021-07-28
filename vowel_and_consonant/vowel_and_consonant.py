input_string = input()
for symbol in input_string:
    if symbol.isalpha():
        if symbol in "aeiou":
            print("vowel")
        else:
            print("consonant")
    else:
        break
