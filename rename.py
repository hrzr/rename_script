#!/usr/bin/python3

import csv
import os
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        if os.path.exists("rename.csv"):
            rename_pattern_file = "rename.csv"
        else:
            raise FileNotFoundError("Can't find `rename.csv`")
    else:
        if os.path.exists(sys.argv[1]):
            rename_pattern_file = sys.argv[1]
        else:
            raise FileNotFoundError(f"Can't find {sys.argv[1]}")
    with open(rename_pattern_file) as rename_pattern:
        file = csv.reader(rename_pattern)
        for line in file:
            if os.path.exists(line[0]) and os.path.isfile(line[0]):
                os.rename(line[0], line[1])
            elif not os.path.exists(line[0]):
                print(f"No such file or directory: {line[0]}")
            elif os.path.isdir(line[0]):
                if input(f"{line[0]} is a directory. Rename anyway?").lower().startswith('y'):
                    os.rename(line[0], line[1])
            else:
                print("Some other error occured")
