import math

def max_prime_factor(number):
    prime_factors = []
    while number % 2 == 0:
        prime_factors.append(2),
        number = number / 2

    for num in range(3, int(math.sqrt(number)) + 1, 2):
        while number % num == 0:
            prime_factors.append(num),
            number = number / num

    if number > 2:
        prime_factors.append(number)

    print(prime_factors[-1])

max_prime_factor(600851475143)


        