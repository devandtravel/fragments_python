def find_repeating_symbols(string):
    word = string.lower()
    result_list = list(')' * len(word))
    if len(set(word)) == len(word):
        result = ')' * len(word)
    else:
        result = ''
        for index, letter in enumerate(word):
            for i in range(len(word) - 1):
                if letter == word[i] and i != index:
                    result_list[index] = '('
                    result_list[i] = '('
    result = ''.join(result_list)
    return result


print(find_repeating_symbols('qqQjaaaa'))
