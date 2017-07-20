#!/usr/bin/env python


def main():
    num_range = range(1, 101)
    sum_of_square = []
    for n in num_range:
        sum_of_square.append(n**2)
    
    sum_of_square = sum(sum_of_square)
    
    square_of_sum = (sum(num_range))**2

    print(sum_of_square)
    print(square_of_sum)
    print(square_of_sum - sum_of_square)


if __name__ == "__main__":
    main()
