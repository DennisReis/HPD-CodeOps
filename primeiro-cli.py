#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("giropops", help="Comanado para possuir mentes", type=int)

args = parser.parse_args()

print(args.giropops)

