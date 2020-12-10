#!/usr/bin/python3

import sys
import argparse
import os
from collections import *

def executeInstructions(instructions):
    """ Execute the instructions in correct sequential
    order until complete or problem identified """
    
    instruct_counter, acc = 0, 0
    executed = set()

    while instruct_counter < len(instructions):
        if instruct_counter in executed:
            """ Completed before last instruction
            exit and update instruction set again """
            return None
        
        executed.add(instruct_counter)
        i, v = instructions[instruct_counter]
        if i == "acc":
            acc += v
            instruct_counter += 1
        elif i == "jmp":
            instruct_counter += v
        else:
            instruct_counter += 1
    
    return acc


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",  help="Input file of bag combinations")

    args = parser.parse_args()

    try:
        with open(args.inputfile, 'r') as f:
            """ Change to aquiring instructions from the file
            including, not injecting execution state """
            instructions = [line.strip().split() for line in f.readlines() if line.strip()]
            instructions = [(i, int(v)) for i, v in instructions]

    except OSError:
        print(f"{args.inputfile} is MISSING!")
    else:
        executed = set()
        instruct_counter, p1 = 0, 0
        print(instructions)
        while instruct_counter not in executed:
            i, v = instructions[instruct_counter]
            print(f"{instruct_counter} is {instructions[instruct_counter]}")
            previous = instruct_counter
            print(f"{i}, {v}")
            if i == "acc":
                p1 += v
                instruct_counter += 1
            elif i == "jmp":
                instruct_counter += v
            else:
                instruct_counter += 1
            executed.add(previous)

        for i in range(len(instructions)):
            if instructions[i][0] == "acc":
                # Do nothing special
                continue
            new_instruction = "jmp" if instructions[i][0] == "nop" else "nop"
            new_instructions = instructions[:i] + [(new_instruction, instructions[i][1])] + instructions[i+1:]
            p2 = executeInstructions(new_instructions)
            if p2 is not None:
                break
            
        print(f"Part 1 answer is {p1}")
        print(f"Part 2 answer is {p2}")

if __name__ == "__main__":
    main()
