#!/usr/bin/env python
import timeit
import sys
import math


def main():

    number = 0
    i = 1

    while number_of_divisors(number) < 500:
        number += i
        i += 1

    print("The first triangle number with over 500 divisors is: " + str(number))


def number_of_divisors(number):
    nod = 0
    sqrt = int(math.sqrt(number))

    for i in range(1, sqrt + 1):
        if number % i == 0:
            nod += 2

    if sqrt * sqrt == number:
        nod -= 1

    return nod


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print("This solution took " + str(timeit.default_timer() - start_time) + " seconds.")
