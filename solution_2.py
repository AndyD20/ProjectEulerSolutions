#!/usr/bin/env python

def main():

    old_term, current_term = 1, 1
    vals = []

    for n in range (1000):
        while (current_term < 4000000):
            old_term, current_term = current_term, old_term + current_term
            if current_term % 2 == 0:
                vals.append(current_term)
    print(vals)
    print (sum(vals))
    


if __name__ == "__main__":
    main()