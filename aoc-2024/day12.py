day=12

from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from copy import deepcopy
from tqdm import tqdm
from itertools import chain, repeat
import networkx as nx
import random

def c_grids_accounted_for(regions):
    s = set()
    for k, v in regions.items():
        for reg in v:
            for gr in reg:
                s.add(gr)
    return len(s)

def neighbors(cellx, celly, nrows, ncols):
    n = set()
    if cellx > 0:
        n.add((cellx-1, celly))
    if cellx < (nrows - 1):
        n.add((cellx+1, celly))
    if celly > 0:
        n.add((cellx, celly - 1))
    if celly < (ncols - 1):
        n.add((cellx, celly + 1))
    return n





def get_region_cells(V, nrows, ncols):
    cells = set()
    for i in range(nrows):
        for j in range(ncols):
            if V[i][j] == ".":
                cells.add((i, j))
    return cells





def first(input):
    M = []

    for line in input.split("\n"):
        M.append(list(line.strip()))

    nrows, ncols = len(M), len(M[0])
    for i in range(nrows):
        print(*M[i], sep=" ")

    regions = {}
    accounted_for = 0
    V = deepcopy(M)
    W = deepcopy(V)
    sx, sy = 0, 0

    def visit(M, V, cellx, celly):
        stack = []
        stack.append((cellx, celly))
        start_color = M[cellx][celly]
        while stack:
            cellx, celly = stack.pop()
            if V[cellx][celly] == ".":
                continue
            V[cellx][celly] = "."
            nei = neighbors(cellx, celly, len(M), len(M[0]))
            for nx, ny in nei:
                if M[nx][ny] == start_color:
                    visit(M, V, nx, ny)
                else:
                    print(f"edge found @ {(nx, ny)}")
                    global edges_in_account
                    edges_in_account.add((nx, ny))
                    global perim
                    perim += 1
        return V

    while (accounted_for) < (nrows * ncols):
        #print(f"region={M[sx][sy]}")
        V = visit(M, V, sx, sy)

        #for i in range(nrows):
        #    print(*V[i], sep=" ")

        if M[sx][sy] not in regions:
            regions[M[sx][sy]] = []

        region_cells = []
        for i in range(nrows):
            for j in range(ncols):
                if V[i][j] != W[i][j]:
                    region_cells.append((i, j))
        W = deepcopy(V)
        regions[M[sx][sy]].append(region_cells)
        accounted_for += len(region_cells)
        #print(f'{accounted_for=}')
        sx, sy = random.randint(0, nrows - 1), random.randint(0, ncols - 1)
        if (accounted_for) < (nrows * ncols):
            while V[sx][sy] == ".":
                sx, sy = random.randint(0, nrows-1), random.randint(0, ncols-1)
        #print("*" * 50)

    a = 0
    price = 0
    for k, v in regions.items():
        for reg in v:
            added = 0
            for grx, gry in reg:
                added += 4
                for nx, ny in neighbors(grx, gry, nrows, ncols):
                    if (nx, ny) in set(reg):
                        added -= 1
            price += (added * len(reg))
            print(k, reg, added)
            a += added
    print(a)
    print(price)

def twotwo(npM, cellx, celly, direction=1):
    val = npM[cellx][celly]
    s = [val]
    cells = []
    if direction == 1:
        s.append(npM[cellx][celly - 1])
        s.append(npM[cellx - 1][celly])
        # atell
        s.append(npM[cellx - 1][celly - 1])
        retcoords = -1, -1
        cells.extend([(cellx, celly), (cellx, celly - 1), (cellx - 1, celly), (cellx - 1, celly - 1)])
    elif direction == 2:
        s.append(npM[cellx][celly + 1])
        s.append(npM[cellx - 1][celly])
        # atell
        s.append(npM[cellx - 1][celly + 1])
        retcoords = -1, 1
        cells.extend([(cellx, celly), (cellx, celly + 1), (cellx - 1, celly), (cellx - 1, celly + 1)])
    elif direction == 3:
        s.append(npM[cellx][celly - 1])
        s.append(npM[cellx + 1][celly])
        # atell
        s.append(npM[cellx + 1][celly - 1])
        retcoords = 1, -1
        cells.extend([(cellx, celly), (cellx, celly - 1), (cellx + 1, celly), (cellx + 1, celly - 1)])
    elif direction == 4:
        s.append(npM[cellx][celly + 1])
        s.append(npM[cellx + 1][celly])
        # atell
        s.append(npM[cellx + 1][celly + 1])
        retcoords = 1, 1
        cells.extend([(cellx, celly), (cellx, celly + 1), (cellx + 1, celly), (cellx + 1, celly + 1)])

    cs = Counter(s)
    if (cs[val] == 3):
        print("HARMAS")
        print(cellx - 1, celly - 1, val, direction)

        return "h", tuple(sorted(cells) + ["h"])
    if (cs[val] == 1):
        print("EGYES")
        print(cellx - 1, celly - 1, val, direction)

        return "e", tuple(sorted(cells) + ["e"])
    if ((cs[val] == 2) and (val not in s[1:3])):
        print("ATELLEN!")
        print(cellx-1, celly-1, val, direction)

        return "ae", tuple(sorted(cells) + ["ae"+str(random.randint(0,235235252))])

    return None, []




def second(input):
    M = []

    for line in input.split("\n"):
        M.append(list(line.strip()))

    nrows, ncols = len(M), len(M[0])
    for i in range(nrows):
        print(*M[i], sep=" ")

    regions = {}
    accounted_for = 0
    V = deepcopy(M)
    W = deepcopy(V)
    sx, sy = 0, 0

    def visit(M, V, cellx, celly):
        stack = []
        stack.append((cellx, celly))
        start_color = M[cellx][celly]
        while stack:
            cellx, celly = stack.pop()
            if V[cellx][celly] == ".":
                continue
            V[cellx][celly] = "."
            nei = neighbors(cellx, celly, len(M), len(M[0]))
            for nx, ny in nei:
                if M[nx][ny] == start_color:
                    visit(M, V, nx, ny)
                else:
                    print(f"edge found @ {(nx, ny)}")
                    global edges_in_account
                    edges_in_account.add((nx, ny))
                    global perim
                    perim += 1
        return V

    npM = np.pad(np.array(M), (1,1)).tolist()

    while (accounted_for) < (nrows * ncols):
        #print(f"region={M[sx][sy]}")
        V = visit(M, V, sx, sy)

        #for i in range(nrows):
        #    print(*V[i], sep=" ")

        if M[sx][sy] not in regions:
            regions[M[sx][sy]] = []

        region_cells = []
        for i in range(nrows):
            for j in range(ncols):
                if V[i][j] != W[i][j]:
                    region_cells.append((i, j))
        W = deepcopy(V)
        regions[M[sx][sy]].append(region_cells)
        accounted_for += len(region_cells)
        print(f'{accounted_for=}')
        sx, sy = random.randint(0, nrows - 1), random.randint(0, ncols - 1)
        if (accounted_for) < (nrows * ncols):
            while V[sx][sy] == ".":
                sx, sy = random.randint(0, nrows-1), random.randint(0, ncols-1)
        #print("*" * 50)

    npM = np.pad(np.array(M), (1, 1)).tolist()
    price = 0
    for k, v in regions.items():
        if k == 0: continue
        for reg in v:
            cvx, ccv = 0, 0
            print(k, reg)
            corners = set()
            for grx, gry in reg:
                for i in range(1, 5):
                    t, cells = twotwo(npM, grx+1, gry+1, i)
                    if t:
                        corners.add(cells)

            #print('lc', len(corners))
            numsides = len(corners)
            price += numsides * len(reg)
            print()

    print(price)

887932

global perim
perim = 0
global edges_in_account
edges_in_account = set()
data = Path(f"day{day}.input").read_text()
example = """AAAA
BBCD
BBCC
EEEC"""

example2 = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

example3 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

example4 = '''AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA'''
second(data)

#second(data)
#first(data)
