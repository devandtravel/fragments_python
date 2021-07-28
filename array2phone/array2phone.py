import re


def array2phone(array):
    return f"({array[0]}{array[1]}{array[2]}) {array[3]}{array[4]}{array[5]}-{array[6]}{array[7]}{array[8]}{array[9]}"


print(array2phone([9, 9, 9, 1, 2, 3, 4, 5, 6, 7]))

print('(%s) %s-%s' % tuple(
    re.findall(r'\d{4}$|\d{3}', ''.join(
        map(str, [9, 9, 9, 1, 2, 3, 4, 5, 6, 7])))))
