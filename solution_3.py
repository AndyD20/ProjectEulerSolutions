#!/usr/bin/env python


def main():
    primes = [2]
    current_highest = 3

    for n in range(3, 10000):

        if n > 2 and n % 2 == 0 or n > 3 and n % 3 == 0 or n > 5 and n % 5 == 0 or n > 7 and n % 7 == 0:
            pass
        else:
            is_prime = True
            for p in primes:
                if n % p == 0:
                    is_prime = False

            if is_prime:
                if 600851475143 % p == 0:
                    current_highest = p
                primes.append(n)

    print(current_highest)


if __name__ == "__main__":
    main()
