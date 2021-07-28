number = int(input())
is_prime = True
for n in range(2, number):
    if (number <= 1) or (number % n == 0):
        is_prime = False
print("This number is prime" if is_prime else "This number is not prime")