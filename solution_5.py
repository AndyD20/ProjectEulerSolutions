#!/usr/bin/env pypy

import timeit
import sys

target_length = int(sys.argv[1])
target_list = range(target_length, target_length - (target_length / 2), -1)
print target_list

def main():

    search_range = range(0, target_length * 100000000, target_length)
    search_range.remove(0)
    print len(search_range)

    for i in search_range:
        if all(i % x == 0 for x in target_list):
            print(i)
            break
        
        
if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print("This solution took " + str(timeit.default_timer() - start_time) + " seconds.")
