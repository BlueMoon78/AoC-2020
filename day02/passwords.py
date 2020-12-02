#!/usr/bin/python3

import sys
import argparse
import re

def check_password(input, check):
    s_line = re.split(r"\s",input)
    
    # First find the required range
    numbers = re.split("-",s_line[0])
    minimum = int(numbers[0])
    maximum = int(numbers[1])

    # What character are we seaching for?
    tmp = re.split(":",s_line[1])
    key = tmp[0]

    # Get the character count
    keys = re.findall(key, s_line[2])
    count = len(keys)

    # Strip the password as a list for inspection
    password = []
    password[:0] = s_line[2]
    password_len = len(password) # Used as a safety net for array bounds

    if not check and minimum <= count <= maximum:
        # Old password method validates
        return True
    elif check and count == 1 and password[minimum - 1] == key:
        # New password method, only one match and its first reference
        return True
    elif check and maximum <= password_len:
        # New password method, second reference is within list length
        if count == 1 and password[maximum - 1] == key:
            # Only one instance and it matches second reference
            return True
        elif count > 1 and password[minimum - 1] == key\
            and password[maximum - 1] != key:
            # Single correct match
            return True
        elif count > 1 and password[minimum - 1] != key\
            and password[maximum - 1] == key:
            # Single correct match
            return True
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",  help="Input file of corrupted passwords")
    parser.add_argument("-n", "--new", help="For checking with the updated password policy", action="store_true", default=False)

    args = parser.parse_args()
    matches = 0

    try:
        with open(args.inputfile) as f:
            for line in f:
                if check_password(line, args.new):
                    matches += 1
    except OSError:
        print(f"Cannot open {args.inputfile}\n")
    else:
        print(f"Number of matches: {matches}\n")

if __name__ == "__main__":
    main()
