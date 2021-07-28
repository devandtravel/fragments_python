my_array = [1, 56, 32, 6, 56, 34, 86798, 23, 54]
flag = 1
while flag == 1:
  flag = 0
  for index, item in enumerate(my_array):
    if index <= len(my_array) - 2:
      if (item > my_array[index + 1]):
        temp = my_array[index]
        my_array[index] = my_array[index + 1]
        my_array[index + 1] = temp
        flag = 1
print(my_array)