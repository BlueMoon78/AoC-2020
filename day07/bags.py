#!/usr/bin/python3

import sys
import argparse
import os
from collections import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",  help="Input file of bag combinations")
    parser.add_argument("--bag", "-b",   help="Type of bag being searched for, e.g. \"shiny gold\" (the default)", type=str, default="shiny gold")

    args = parser.parse_args()

    search_key = tuple(s for s in args.bag.split())

    try:
        with open(args.inputfile, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            first = defaultdict(list)
            first_rev = defaultdict(list)

            for line in lines:
                bag, contains = line.split(" bags contain ")
                bag = tuple(bag.split())
                
                if contains.startswith("no"):
                    # no types of bag stored in bag
                    continue

                contains = contains.split(", ")
                first[bag] = [(int(c.split()[0]), tuple(c.split()[1:-1])) for c in contains]
                for _, c in first[bag]:
                    # Get the list of bag type is in bags for P1
                    first_rev[c].append(bag)
                
            tmp = deque([search_key])
            p1 = set([tuple(x) for x in tmp])
            while tmp:
                item = tmp.popleft()
                for bags in first_rev[item]:
                    if bags not in p1:
                        tmp.append(bags)
                        p1.add(bags)
            """Remember to discard the original bag if it is
            still there!!"""
            p1.discard(search_key)

    except OSError:
        print(f"{args.inputfile} is MISSING!")
    else:
        print(f"Part 1 answer is {len(p1)}")
        
        def totalBags(bag):
            """ Recursive function to go through all bag types
            found in the target outer bag, along with the bag types
            found in those and so on...."""
            p2 = 1 # Necessary evil to cope with multiply by 0
            for number, bag_type in first[bag]:
                p2 += number * totalBags(bag_type)
            return p2
        
        p2 = totalBags(search_key) - 1 # Is there a better way to get around 0 multplication!!?
        print(f"Part 2 answer is {p2}")

if __name__ == "__main__":
    main()
