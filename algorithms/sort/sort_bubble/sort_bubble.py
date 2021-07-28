def sort_bubble(arr):
    n = len(arr)
    # i : 1 -> n
    for i in range(n):
        # j -> n -i -1 , -1 for the j+1 comparison of last element
        for j in range(0, n - i - 1):
            # if current is bigger than next
            if arr[j] > arr[j + 1]:
                # swap current and next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(sort_bubble([1, 56, 32, 6, 56, 34, 86798, 23, 54]))
