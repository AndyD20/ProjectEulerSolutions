#!/usr/bin/env python
import timeit, maths_helper


def main():
    prime_list = maths_helper.primesfrom2to(2000000)
    print sum(prime_list)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print("This solution took " + str(timeit.default_timer() - start_time) + " seconds.")
