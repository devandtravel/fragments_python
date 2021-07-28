def pig_it(input_string):
    result_string = ''

    for word in input_string.split(' '):
        template = 'ay'
        result_word = word[1:] + word[0] + template
        result_string = result_string + ' ' + result_word
    return result_string


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))