#!/usr/bin/env python
import sys


def main():

    total = 0

    for n in range(0, int(sys.argv[1])):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    
    print(total)


if __name__ == "__main__":
    main()
