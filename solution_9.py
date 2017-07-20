#!/usr/bin/env pypy
import timeit

def main():
    for i in range(1, 1000):
        for j in range(1, 1000):
            for k in range(1, 1000):
                if i + j + k == 1000 and i**2 + j**2 == k**2:
                    print ("a = " + str(i) + "; b = " + str(j) + "; c = " + str(k))

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print("This solution took " + str(timeit.default_timer() - start_time) + " seconds.")
