import argparse
import re
import os

parser = argparse.ArgumentParser()

parser.add_argument('-f', metavar='file', type=str, required=True, help='input file')
parser.add_argument('header', type=str)
parser.add_argument('key', type=str)
parser.add_argument('value', type=str)
args = parser.parse_args()

if os.path.isfile(args.f) \
    and args.header is not None \
    and len(args.header) > 0 \
    and args.key is not None \
    and len(args.key) > 0 \
    and args.value is not None \
    and len(args.value) > 0:
    items = []
    current_item = None
    with open(args.f) as f:
        for l in f:
            if re.match(r'^\[[\w-]+\]$', l):
                if current_item is not None:
                    items.append(current_item)
                current_item = [l.strip(),[]]
            else:
                if current_item is not None and l is not None:
                    tup = [v.strip() for v in l.strip().split('=')]
                    if current_item[0] == f"[{args.header}]" and len(tup) == 2 and tup[0] == args.key:
                        current_item[1].append(f'{tup[0]} = {args.value}')
                    elif len(l.strip()) > 0:
                        current_item[1].append(l.strip())
        if current_item is not None:
            items.append(current_item)
    with open(args.f, 'w') as f:
        for item in items:
            f.write(item[0] + "\n")
            for line in item[1]:
                f.write(line + "\n")
            f.write("\n")
