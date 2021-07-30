import numpy as np

print('input a number')
get_cumulative_sum_list = np.fromiter(input(), int).cumsum().tolist()
print('using numpy')
print(get_cumulative_sum_list)

print('input a number')
number = [int(s) for s in input()]
print('using list comprehension')
print([sum(number[:i + 1]) for i in range(len(number))])