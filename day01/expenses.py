#!/usr/bin/python3

import sys
from itertools import combinations
import numpy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input",  help="Input file of integers")
parser.add_argument("--target",   help="Target", type=int, default=2020)

args = parser.parse_args()

expenses = []
with open( args.input ) as f:
  for line in f:
    expenses.append(int(line)) # Cvonvert to int[] from input file

part1, part2 = 2, 3 # The number of cnumbers combined to make target

# First lets check Part 1
combis = combinations(expenses, part1)
for c in combis:
  if sum(c) == args.target:
    print(f"The product for Part 1 is {numpy.prod(c)}")
    break

# Finaly lets check Part 2
combis = combinations(expenses, part2)
for c in combis:
  if sum(c) == args.target:
    print(f"The product for Part 2 is {numpy.prod(c)}")
    break
