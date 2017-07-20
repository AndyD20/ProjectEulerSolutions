#!/usr/bin/env python


def main():
    palindrome = 0

    for num_1 in range(1000):
        for num_2 in range(1000):
            product = num_1*num_2
            if is_palindrome(product) and product > palindrome:
                palindrome = product

    print(palindrome)


def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True

if __name__ == "__main__":
    main()
