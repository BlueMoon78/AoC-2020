#!/usr/bin/python3

import sys
import argparse

def checkForTrees(inputfile, h, v):
    x, y = 0, 0
    tree = '#'
    num_trees = 0
    try:
        with open(inputfile, 'r') as f:  
            for line in f:
                if y%v == 0 and y > 0:
                    x += h
                    tree_line = line.strip()
                    while x >= len(tree_line):
                        tree_line += tree_line
                    if tree_line[x] == tree:
                        num_trees += 1
                y += 1
    except OSError:
        print(f"Cannot open {inputfile}")
        return -1
    else:
        return num_trees

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",  help="Input file of corrupted passwords")

    args = parser.parse_args()

    print(f"Part 1 answer is {checkForTrees(args.inputfile, 3, 1)}")
    p2a = checkForTrees(args.inputfile, 1, 1)
    p2b = checkForTrees(args.inputfile, 3, 1)
    p2c = checkForTrees(args.inputfile, 5, 1)
    p2d = checkForTrees(args.inputfile, 7, 1)
    p2e = checkForTrees(args.inputfile, 1, 2)
    p2 = p2a * p2b * p2c * p2d * p2e
    print(f"Part 2 answer is {p2}")

if __name__ == "__main__":
    main()
