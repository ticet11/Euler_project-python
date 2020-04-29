"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_multiples():
    sum_list = []
    max_number = input('What should the max number be?:')
    for num in range(int(max_number)):
        if num % 3 == 0 or num % 5 == 0:
            sum_list.append(num)

    print(sum(sum_list))


sum_of_multiples()
