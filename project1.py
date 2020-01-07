# Project Euler Problem 1
# Multiples of 3 and 5

''' If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. '''

# python 3

mult_of_3 = [i for i in range(3, 1000, 3)]

mult_of_5 = [i for i in range(5, 1000, 5)]

print(sum(set(mult_of_3 + mult_of_5)))

# output = 233168