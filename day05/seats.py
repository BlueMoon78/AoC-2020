#!/usr/bin/python3

import sys
import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",  help="Input file of corrupted passwords")

    args = parser.parse_args()

    p1 = 0
    seats = []

    try:
        with open(args.inputfile, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            p1 = 0

            for line in lines:
                low = 0
                high = 1 << 7
                for c in line[:7]:
                    mid = (low + high) // 2
                    if c == "F": high = mid
                    else: low = mid
                
                left = 0
                right = 1 << 3
                for c in line[7:]:
                    mid = (left + right) // 2
                    if c == "L": right = mid
                    else: left = mid

                seat = (low * 8) + left
                seats.append(seat)
                p1 = max(p1, seat)
    except OSError:
        print(f"{args.inputfile} is MISSING!")
    else:
        seats.sort()
        i, j = 0, 1
        while seats[j] - seats[i] != 2:
            i += 1
            j += 1
        p2 = seats[i] + 1
        print(f"Part 1 answer is: {p1}")
        print(f"Part 2 answer is: {p2}")

if __name__ == "__main__":
    main()
