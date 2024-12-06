from collections import Counter
from pathlib import Path

import networkx
import numpy as np
from copy import deepcopy
from tqdm import tqdm
from itertools import chain, repeat
import networkx as nx

# diagonal

# written backwards
# overlapping

directions = {
    "u": (-1, 0),
    "r": (0, 1),
    "d": (1, 0),
    "l": (0, -1)
}
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def first(input):
    M = []

    for line in input.split("\n"):
        M.append(list(line.strip()))

    nrows, ncols = len(M), len(M[0])

    currx, curry = 0, 0
    for i in range(nrows):
        for j in range(ncols):
            if M[i][j] == "^":
                currx = i
                curry = j
                break
    print((currx, curry))

    visited = set()
    visited.add((currx, curry))
    M[currx][curry] = "."
    diridx = 0

    while (0 <= currx < nrows) and (0 <= curry < ncols):
        newx, newy = currx + dirs[diridx][0], curry + dirs[diridx][1]
        if (newx >= nrows) or (newy >= ncols) or (newx < 0) or (newy < 0):
            break

        while M[newx][newy] == "#":
            diridx = (diridx + 1) % 4
            newx, newy = currx + dirs[diridx][0], curry + dirs[diridx][1]
        visited.add((newx, newy))
        currx, curry = newx, newy

    print(len(visited))
    return visited


def second(input):
    M = []

    for line in input.split("\n"):
        M.append(list(line.strip()))

    nrows, ncols = len(M), len(M[0])

    currx, curry = 0, 0
    for i in range(nrows):
        for j in range(ncols):
            if M[i][j] == "^":
                currx = i
                curry = j


    print((currx, curry))
    startx, starty = currx, curry
    M[currx][curry] = "."

    knownpath = first(input)
    pot_obs = set(knownpath)
    for p in knownpath:
        for i in range(4):
            newx, newy = p[0] + dirs[i][0], p[1] + dirs[i][1]
            if (0 <= newx < nrows) and (0 <= newy < ncols):
                if M[newx][newy] != "#":
                    pot_obs.add((newx, newy))


    print(pot_obs)
    good_obs = set()
    good_cycles = set()
    for obsx, obsy in tqdm(pot_obs):
        M[obsx][obsy] = "#"

        visited = set()
        visited.add((startx, starty))
        diridx = 0
        currx, curry = startx, starty
        iter = 50000
        while (0 <= currx < nrows) and (0 <= curry < ncols) and (iter > 0):
            newx, newy = currx + dirs[diridx][0], curry + dirs[diridx][1]
            if (newx >= nrows) or (newy >= ncols) or (newx < 0) or (newy < 0):
                #print(f"{iter} out of the map!!!")
                break

            while M[newx][newy] == "#":
                diridx = (diridx + 1) % 4
                newx, newy = currx + dirs[diridx][0], curry + dirs[diridx][1]
            visited.add((newx, newy))
            currx, curry = newx, newy
            iter -= 1

        if iter == 0:
            #print(f"ooooooooooooo")
            good_obs.add((obsx, obsy))

        M[obsx][obsy] = "."

    #print(len(visited))
    #print(metobs)
    print(len(good_obs), good_obs)
    #print(len(good_cycles))
    #print(good_cycles)



if __name__ == "__main__":
    data = Path(f"day6.input").read_text()
    example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    #second(example)

    second(data)
    #first(data)


# 1.
# 5081 too high
# 2.
#