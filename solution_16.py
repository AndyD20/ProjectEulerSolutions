#!/usr/bin/env python
import timeit


def main():
    real_big_number = list(str(2 ** 1000))
    real_big_sum = 0

    for i in real_big_number:
        real_big_sum += int(i)

    print(real_big_sum)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print("This solution took " + str(timeit.default_timer() - start_time) + " seconds.")
