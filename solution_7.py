#!/usr/bin/env pypy
import timeit


def main():
    primes = [2]
    
    for n in range(3, 120000, 2):
        
        if n > 3 and n % 3 == 0 or n > 5 and n % 5 == 0 or n > 7 and n % 7 == 0:
            pass
        else:
            is_prime = True
            for p in primes:
                if n % p == 0:
                    is_prime = False
            
            if is_prime:
                primes.append(n)
    print(primes[10000])

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print("This solution took " + str(timeit.default_timer() - start_time) + " seconds.")
