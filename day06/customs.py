#!/usr/bin/python3

import sys
import argparse
import os
from collections import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",  help="Input file of corrupted passwords")

    args = parser.parse_args()

    try:
        with open(args.inputfile, 'r') as f:
            lines = f.read().split("\n\n")
            p1, p2 = 0, 0

            for line in lines:
                c = Counter(line)
                p1 += len(c)
                if "\n" in c:
                    p1 -= 1
                
                l = len(line.split())
                c = Counter(line)
                p2 += sum(v == l for _, v in c.items())
                if c['\n'] == l:
                    p2 -= 1
                
    except OSError:
        print(f"{args.inputfile} is MISSING!")
    else:
        print(f"Part 1 answer is {p1}")
        print(f"Part 2 answer is {p2}")

if __name__ == "__main__":
    main()
