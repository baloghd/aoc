day=10

from collections import Counter
from pathlib import Path

import numpy as np
from copy import deepcopy
from tqdm import tqdm
from itertools import chain, repeat

import networkx as nx

def first(input):
    M = []

    for line in input.split("\n"):
        M.append(list(line.strip()))

    nrows, ncols = len(M), len(M[0])

    G = nx.Graph()
    zeros, nines = [], []
    n_zeros = 0
    for i in range(nrows):
        for j in range(ncols):
            c =  M[i][j]
            if c == '9':
                nines.append((i, j))
            if c == ".": continue
            if c == '0':
                G.add_node((i,j), name=f"0_#{n_zeros}")
                zeros.append((i, j))
                n_zeros += 1
            # fel
            if i > 0:
                if M[i-1][j] != "." and abs(int(M[i-1][j]) - int(c)) == 1:
                    G.add_edge((i, j), (i-1, j))
            # le
            if i < nrows - 1:
                if M[i + 1][j] != "." and abs(int(M[i + 1][j]) - int(c)) == 1:
                    G.add_edge((i, j), (i + 1, j))
            # bal
            if j > 0:
                if M[i][j-1] != "." and abs(int(M[i][j-1]) - int(c)) == 1:
                    G.add_edge((i, j), (i, j-1))
            # jobb
            if j < ncols - 1:
                if M[i][j+1] != "." and abs(int(M[i][j+1]) - int(c)) == 1:
                    G.add_edge((i, j), (i, j+1))

    s = 0
    for zx, zy in tqdm(zeros):
        #print((zx, zy))
        zscore = 0
        for ninx, niny in nines:
            try:
                p = nx.shortest_path(G, source=(zx, zy), target=(ninx, niny))
                # print(p)
                if len(p) == 10:
                    zscore += 1

            except nx.exception.NodeNotFound:
                continue
            except nx.exception.NetworkXNoPath:
                continue
        #print(zscore)
        s += zscore
    print(s)

def second(input):
    M = []

    for line in input.split("\n"):
        M.append(list(line.strip()))

    nrows, ncols = len(M), len(M[0])

    G = nx.Graph()
    zeros, nines = [], []
    n_zeros = 0
    for i in range(nrows):
        for j in range(ncols):
            c =  M[i][j]
            if c == '9':
                nines.append((i, j))
            if c == ".": continue
            if c == '0':
                G.add_node((i,j), name=f"0_#{n_zeros}")
                zeros.append((i, j))
                n_zeros += 1
            # fel
            if i > 0:
                if M[i-1][j] != "." and abs(int(M[i-1][j]) - int(c)) == 1:
                    G.add_edge((i, j), (i-1, j))
            # le
            if i < nrows - 1:
                if M[i + 1][j] != "." and abs(int(M[i + 1][j]) - int(c)) == 1:
                    G.add_edge((i, j), (i + 1, j))
            # bal
            if j > 0:
                if M[i][j-1] != "." and abs(int(M[i][j-1]) - int(c)) == 1:
                    G.add_edge((i, j), (i, j-1))
            # jobb
            if j < ncols - 1:
                if M[i][j+1] != "." and abs(int(M[i][j+1]) - int(c)) == 1:
                    G.add_edge((i, j), (i, j+1))

    s = 0
    for zx, zy in tqdm(zeros):
        print((zx, zy))
        rat = 0
        for ninx, niny in nines:
            try:
                p = nx.all_shortest_paths(G, source=(zx, zy), target=(ninx, niny))
                rating = 0
                for sp in p:
                    if len(sp) == 10:
                        rating += 1
                rat += rating
            except nx.exception.NodeNotFound:
                continue
            except nx.exception.NetworkXNoPath:
                continue
        print(rat)
        s += rat

    print(s)


if __name__ == "__main__":
    data = Path(f"day{day}.input").read_text()
    example = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""

    example2 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

    example3 = '''10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01'''

    example4 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

    example5 = """.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9...."""

    example6 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

    example7 = """012345
123456
234567
345678
4.6789
56789."""



    #first(data)

    second(data)
    # first(data)
