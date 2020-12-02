#!/usr/bin/python3

import sys
from itertools import combinations
import numpy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("inputfile",  help="Input file of integers")
parser.add_argument("--target",   help="Target", type=int, default=2020)
parser.add_argument("--entries",  help="Number of expenses to consider", type=int, default=2)
args = parser.parse_args()

# Slurp integers from file into array
expenses = []
with open( args.inputfile ) as f:
  for line in f:
    expenses.append(int(line))

# Get all combinations in the set
combis = combinations(expenses, args.entries)
for c in combis:
  if sum(c) == args.target:
    print( numpy.prod(c) )
    break
