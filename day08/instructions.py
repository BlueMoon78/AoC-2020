#!/usr/bin/python3

import sys
import argparse
import os
from collections import *



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",  help="Input file of bag combinations")

    args = parser.parse_args()

    try:
        with open(args.inputfile, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            instructions = []
            for line in lines:
                i, q = line.split()
                instructions.append([i, int(q), False])

    except OSError:
        print(f"{args.inputfile} is MISSING!")
    else:
        position = 0
        executed = False
        p1 = 0

        while not executed:
            i, v, executed = instructions[position]
            print(instructions[position])
            if not executed:
                instructions[position][2] = True
                if i == "acc":
                    p1 += v
                    position += 1
                elif i == "jmp":
                    position += v
                else:
                    position += 1

        print(f"Part 1 answer is {p1}")

        # Reset the executted parameter to get P2 answer
        for x in instructions:
            x[2] = False

        position, last_position = 0, 0
        p2 = 0
        change_made = False
        while position < len(instructions):
            i, v, executed = instructions[position]
            if not executed:
                # All is fine, continue
                instructions[position][2] = True
                last_position = position
                if i == "acc":
                    p2 += v
                    position += 1
                elif i == "jmp":
                    position += v
                else:
                    position += 1
            elif not change_made:
                position = last_position
                i, v, executed = instructions[position]
                instructions[position][2] = False
                if i == "jmp": 
                    instructions[position][0] = "nop"
                    change_made = True
                elif i == "nop" :
                    instructions[position][0] = "jmp"
                    change_made = True

                print(f"Change made in line {position + 1}: {instructions[position]}")
            else:
                print("Houston, we have a problem")
                position = len(instructions)

        print(f"Part 2 answer is {p2}")

if __name__ == "__main__":
    main()
