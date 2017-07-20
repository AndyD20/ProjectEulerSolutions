#!/usr/bin/env python
import timeit
import sys


def main():
    with open("numbers.txt", "r") as number_list:
        numbers = number_list.read()

    largest_product = 0
    concurrent_numbers = int(sys.argv[1])

    for n in range(0, len(numbers)):
        if n < len(numbers) - (concurrent_numbers + 1):
            current = 1
            for i in range(n, n + concurrent_numbers):
                current *= int(numbers[i]) 
            if current > largest_product:
                largest_product = current
    print(largest_product)
            

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print("This solution took " + str(timeit.default_timer() - start_time) + " seconds.")
