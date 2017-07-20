#!/usr/bin/env pypy
import timeit, sys


def main():

    triangle_numbers = triangle_numbers_to(int(sys.argv[1]))

    for i in range(0, 10):
        print triangle_numbers[i]
    '''
    for t in triangle_numbers:
        divisors = []
        for i in range (1, int(sys.argv[1])):
            if t % i == 0:
                divisors.append(i)
            
            if len(divisors) > 500:
                print "Solution is: " + str(t)
                print "Index of the triangle number is: " + str(triangle_numbers.index(t))
                print "Length of divisor array was: " + str(len(divisors))
                return
    '''

def triangle_numbers_to(n):
    triangles = []
    for i in range(1, n):
        triangles.append(i*(i+1)/2)
    return triangles

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print("This solution took " + str(timeit.default_timer() - start_time) + " seconds.")
