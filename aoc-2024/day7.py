day=7

from collections import Counter
from pathlib import Path

import numpy as np
from copy import deepcopy
from tqdm import tqdm
from itertools import chain, repeat
import multiprocessing
import networkx as nx
import os
import itertools
import pickle
def getperms(r):
    allops = set()
    for cwr in list(itertools.combinations_with_replacement("MAC", r)):
        for perm in itertools.permutations(cwr):
            allops.add(perm)
    return allops

if os.path.exists("perms.pickle"):
    print("pickle exists!")
    with open("perms.pickle", "rb") as infile:
        perms = pickle.load(infile)
else:
    print("no pickle, working on it...")
    perms = {
        r: getperms(r) for r in range(1, 12)
    }

    with open("perms.pickle", "wb") as outfile:
        pickle.dump(perms, outfile)
        print("pickle dumped!")

def evaluate_single(res, parts, ops) -> bool:
    if ops[0] == "A":
        c = parts[0] + parts[1]
    elif ops[0] == "M":
        c = parts[0] * parts[1]
    elif ops[0] == "C":
        c = int(str(parts[0]) + str(parts[1]))
    else:
        c = 0

    for i in range(1, len(ops)):
        if ops[i] == "A":
            c *= parts[i+1]
        elif ops[i] == "M":
            c += parts[i+1]
        elif ops[i] == "C":
            c = int(str(c)+str(parts[i+1]))
        if c > res:
            break
    #print(c)
    return c == res

def job(*args):
    res, parts = args[0]
    opslists = perms[len(parts)-1]
    opsthatequals = False
    for ops in opslists:
        ev = evaluate_single(res, parts, ops)
        if ev:
            opsthatequals = True
            break
    if opsthatequals:
        return True

def first(input):
    eqs = []

    for line in input.split("\n"):
        if len(line) > 0:
            res, parts = line.strip().split(":")
            res = int(res)
            parts = list(map(int, parts.strip().split(" ")))
            eqs.append([res, parts])

    s = 0

    pool = multiprocessing.Pool(12)
    results = pool.map(job, eqs)

    for (res, _), boolres in zip(eqs, results):
        if boolres:
            s += res
    print(s)

if __name__ == "__main__":
    data = Path(f"day{day}.input").read_text()
    example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    # second(example)

    #second(data)
    first(data)
