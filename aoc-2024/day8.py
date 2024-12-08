day=8

from collections import Counter
from pathlib import Path

import numpy as np
from copy import deepcopy
from tqdm import tqdm
from itertools import chain, repeat, combinations
import networkx as nx

def dmanh(x, y):
    return y[0] - x[0], y[1] - x[1]

def first(input):
    M = []

    for line in input.split("\n"):
        M.append(list(line.strip()))

    nrows, ncols = len(M), len(M[0])

    coordmap = {}
    for i in range(nrows):
        print(*M[i], sep=" ")

    for i in range(nrows):
        for j in range(ncols):
            c = M[i][j]
            if c != ".":
                if c not in coordmap:
                    coordmap[c] = []
                coordmap[c].append((i, j))

    antinodes = set()
    for key, cs in coordmap.items():
        #if key != "0": continue
        for a, b in combinations(cs, 2):
            print(a,b)
            dist = dmanh(a, b)
            # before smaller
            antix, antiy = a[0] - dist[0], a[1] - dist[1]
            if (antix >= nrows) or (antiy >= ncols) or (antix < 0) or (antiy < 0):
                pass
            else:
                antinodes.add((antix, antiy))
            # after larger
            antix, antiy = b[0] + dist[0], b[1] + dist[1]
            if (antix >= nrows) or (antiy >= ncols) or (antix < 0) or (antiy < 0):
                pass
            else:
                antinodes.add((antix, antiy))

    print(len(antinodes))
    for ax, ay in antinodes:
        M[ax][ay] = "#"

    for i in range(nrows):
        print(*M[i], sep=" ")

def second(input):
    M = []

    for line in input.split("\n"):
        M.append(list(line.strip()))

    nrows, ncols = len(M), len(M[0])

    coordmap = {}
    for i in range(nrows):
        print(*M[i], sep=" ")

    for i in range(nrows):
        for j in range(ncols):
            c = M[i][j]
            if c != ".":
                if c not in coordmap:
                    coordmap[c] = []
                coordmap[c].append((i, j))

    antinodes = set()
    for key, cs in coordmap.items():
        #if key != "0": continue
        for a, b in combinations(cs, 2):
            print(a,b)
            dist = dmanh(a, b)
            # before smaller
            antix, antiy = a[0] - dist[0], a[1] - dist[1]
            while (nrows > antix >= 0) and (ncols > antiy >= 0):
                antinodes.add((antix, antiy))
                antix, antiy = antix - dist[0], antiy - dist[1]

            antix, antiy = a[0] + dist[0], a[1] + dist[1]
            while (nrows > antix >= 0) and (ncols > antiy >= 0):
                antinodes.add((antix, antiy))
                antix, antiy = antix - dist[0], antiy - dist[1]


            # after larger
            antix, antiy = b[0] + dist[0], b[1] + dist[1]
            while (nrows > antix >= 0) and (ncols > antiy >= 0):
                antinodes.add((antix, antiy))
                antix, antiy = antix + dist[0], antiy + dist[1]

            antix, antiy = b[0] - dist[0], b[1] - dist[1]
            while (nrows > antix >= 0) and (ncols > antiy >= 0):
                antinodes.add((antix, antiy))
                antix, antiy = antix + dist[0], antiy + dist[1]


    print(len(antinodes))
    for ax, ay in antinodes:
        M[ax][ay] = "#"

    for i in range(nrows):
        print(*M[i], sep=" ")

if __name__ == "__main__":
    data = Path(f"day{day}.input").read_text()
    example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    second(data)

    #second(data)
    #first(data)
