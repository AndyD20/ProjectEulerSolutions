#!/usr/bin/env python
import timeit


def main():

    longest_chain = []
    number = 0
    for i in range(1000000, 2, -1):
        num_sequence = sequence(i)
        if len(num_sequence) > len(longest_chain):
            longest_chain = num_sequence
            number = i
    print("The number that produces the longest chain is: %s" % number)


def sequence(number):

    num_sequence = [number]

    while number > 1:
        if number % 2 == 0:
            number /= 2
            num_sequence.append(int(number))
        else:
            number = number * 3 + 1
            num_sequence.append(int(number))

    return num_sequence


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print("This solution took " + str(timeit.default_timer() - start_time) + " seconds.")
