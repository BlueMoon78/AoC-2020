#!/usr/bin/python3

import sys
import argparse
import os
from itertools import combinations
# from collections import *

def findSet(parameters, length, match):
    s = 0
    f = s + length
    while f < len(parameters):
        if sum(parameters[s:f]) == match:
            return min(parameters[s:f]) + max(parameters[s:f])
        s += 1
        f = s + length
    return 0



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",  help="Input file of encryption sequence")
    parser.add_argument("--preamble", "-p",   help="Length of preamble, default is 3", type=int, default=25)

    args = parser.parse_args()

    try:
        with open(args.inputfile, 'r') as f:
            """ First extract the numbers into a list
            for searching """
            parameters = [int(line.strip()) for line in f.readlines() if line.strip()]

    except OSError:
        print(f"{args.inputfile} is MISSING!")
    else:
        p1 = 0
        p2 = 0

        input_start = 0
        check = args.preamble
        match = True

        while match:

            combis = combinations(parameters[input_start:check], 2)
            matches = [(sum(c)) for c in combis]
            if parameters[check] not in matches:
                p1 = parameters[check]
                match = False
            input_start += 1
            check += 1
            matches.clear()
        
        length = 2

        while p2 == 0:
            p2 = findSet(parameters, length, p1)
            length += 1

            
        print(f"Part 1 answer is {p1}")
        print(f"Part 2 answer is {p2}")

if __name__ == "__main__":
    main()
