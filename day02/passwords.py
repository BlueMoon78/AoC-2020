#!/usr/bin/python3

import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",  help="Input file of corrupted passwords")

    args = parser.parse_args()
    part1, part2 = 0, 0

    try:
        with open(args.inputfile) as f:
            for line in f:
                n, key, password = line.split()
                key = key[0]
                first, second = map(int, n.split("-"))

                # For part 1, keet iterating the number found based on
                # the requirements being met
                part1 += first <= password.count(key) <= second

                # Now check if only one of the letters is correctly
                # positioned based on the requirements.  Assuming the
                # second position is not outside the string.
                c = 0
                for x in (first, second):
                    if password[x - 1] == key:
                        c += 1
                if c == 1:
                    part2 += 1
    except OSError:
        print(f"Cannot open {args.inputfile}\n")
    else:
        print(f"Number of matches in Part 1: {part1}")
        print(f"Number of matches in Part 2: {part2}")

if __name__ == "__main__":
    main()
