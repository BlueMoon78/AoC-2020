#!/usr/bin/python3

import sys
import argparse
import yaml
import os
import shutil

passport_sep = "---"

class ValidatePassports:

    def __init__(self, library):
        ''' Not the best solution, but a deliberate experiment
        in handling messy data and yaml dictionaries.

        Start by initialising the data from the validation
        library into local sets for comparison. '''

        self.library = library
        with open(self.library, 'r') as stream:
            library_dict = yaml.safe_load(stream)
        self.lib_entries = []
        for elem in library_dict:
            elem_dict = library_dict[elem]
            if elem_dict["mandatory"]:
                self.lib_entries.append(elem)
        self.validation = []
        self.vdata_acquired = False
    
    def generatePassports(self, inputfile):
        passport_num = 0
        passports = {}

        passport_dir = f".{os.sep}passports"
        if os.path.isdir(passport_dir):
            shutil.rmtree(passport_dir)
            os.makedirs(passport_dir)

        with open(inputfile, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            lines.append("") # Temp hack as otherwise the last entry is ignored
            for line in lines:
                if not line:
                    p_file = f"{passport_dir}{os.sep}Passport-{str(passport_num).zfill(4)}.yaml"
                    try:
                        with open(p_file, 'w') as pf:
                            yaml.dump(passports, pf)
                            passports.clear()
                            passport_num += 1
                    except OSError:
                        print(f"{p_file} not found!!")
                else:
                    items = line.split()
                    for s in items:
                        k, v = s.split(":")
                        passports[k] = v
        
        return passport_dir

    def _getDataReqs(self):
        with open(self.library, 'r') as lin:
            library_dict = yaml.safe_load(lin)

        for elem in library_dict:
            self.validation.append(elem)
            self.validation.append(library_dict.get(elem))

        return True
    
    def validatePart1(self, inputfile):
        try:
            with open(inputfile, 'r') as fin:
                p_dict = yaml.safe_load(fin)
                return all(elem in p_dict for elem in self.lib_entries)
        except OSError:
            print(f"{inputfile} is MISSING!!")
            return False
    
    def validatePart2(self, inputfile):
    
        try:
            with open(inputfile, 'r') as fin:
                p_dict = yaml.safe_load(fin)
        except OSError:
            print(f"{inputfile} is MISSING!!")
            return False
        
        if not self.vdata_acquired:
            self.vdata_acquired = self._getDataReqs()
        
        valid = True
        print(p_dict)

        for item in self.lib_entries:
            v_dict = self.validation[self.validation.index(item) + 1]
            if v_dict["type"] == "year":
                valid = valid and v_dict["min"] <= int(p_dict[item]) <= v_dict["max"]
                if valid: print(f"{item} = {valid}, {p_dict[item]}, {v_dict['min']} - {v_dict['max']}")
            elif v_dict["type"] == "length":
                if len(p_dict[item]) >= 3:
                    low = f"{p_dict[item][len(p_dict[item])-2:]}_min"
                    high = f"{p_dict[item][len(p_dict[item])-2:]}_max"
                    valid = valid and v_dict[low] <= int(p_dict[item][:-2]) <= v_dict[high]
                else:
                    valid = False
                if valid: print(f"{item} = {valid}, {p_dict[item]}, {v_dict[low]} - {v_dict[high]}")
            elif v_dict["type"] == "hex":
                valid = valid and len(p_dict[item]) == v_dict["length"]
                valid = valid and p_dict[item][0] == "#"
                valid = valid and all(c in v_dict["valid_char"] for c in p_dict[item][1:])
                if valid: print(f"{item} = {valid}, {p_dict[item]}")
            elif v_dict["type"] == "colour":
                valid_char = []
                for elem in v_dict:
                    if elem not in ["type", "mandatory"]:
                        valid_char.append(v_dict[elem])
                valid = valid and p_dict[item] in valid_char
                valid_char.clear()
                if valid: print(f"{item} = {valid}, {p_dict[item]}")
            elif v_dict["type"] == "number":
                valid = valid and len(p_dict[item]) == v_dict["length"] and all(c in v_dict["valid_char"] for c in p_dict[item])
                if valid: print(f"{item} = {valid}, {p_dict[item]}")
        return valid


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",  help="Input file of corrupted passwords")
    parser.add_argument("--library", "-l", default="library.yaml",
                        help="The library file for validating passport\
                        information", dest="library")

    args = parser.parse_args()

    if not os.path.exists(args.inputfile):
        print(f"File is missing!! {args.inputfile}")
        sys.exit()
    elif not os.path.exists(args.library):
        print(f"File is missing!! {args.library}")
        sys.exit()
    else:
        passport = ValidatePassports(args.library)
        passport_dir = passport.generatePassports(args.inputfile)

        p1, p2 = 0, 0
        
        for files in os.scandir(passport_dir):
            filename = os.path.realpath(files)
            if filename.endswith(".yaml"):
                if passport.validatePart1(filename):
                    p1 += 1
                    if passport.validatePart2(filename):
                        print(f"{filename} PASS\n")
                        p2 += 1
                    else:
                        print("FAIL\n")
        
        print(f"Part 1 answer is: {p1}")
        print(f"Part 2 answer is: {p2}")

if __name__ == "__main__":
    main()
