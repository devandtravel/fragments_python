def pigIt(input_string):
    result_string = ''

    for word in input_string.split(' '):
        template = 'ay'
        result_word = word[1:] + word[0] + template
        result_string = result_string + ' ' + result_word
    return result_string


print(pigIt('Pig latin is cool'))
print(pigIt('Hello world !'))