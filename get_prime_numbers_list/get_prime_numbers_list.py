number = 1000
prime_numbers = []
for i in range(2, number + 1):
    if all(i % n for n in range(2, i)):
        prime_numbers.append(i)
print(prime_numbers)