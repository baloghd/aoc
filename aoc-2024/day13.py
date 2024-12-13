day=13

from collections import Counter
from pathlib import Path
import numpy as np
from copy import deepcopy
from tqdm import tqdm
from itertools import chain, repeat
import networkx as nx
import math
from box import Box
def solve(c):
    # c.A, c.B

    xsteps = 100 #max(c.P.x // c.A.x, c.P.x // c.B.x)
    ysteps = 100 #max(c.P.y // c.A.y, c.P.y // c.B.y)

    C = []
    cost = 0
    for x in range(xsteps):
        r = []
        for y in range(ysteps):
            if ((x * c.A.x + y * c.B.x) == c.P.x) and ((x * c.A.y + y * c.B.y) == c.P.y):
                print(f"{c.P=}, {x,y}, {(3*x) + y}")
                return (3*x) + y
            r.append((3*x) + y)
        C.append(r)
    return 0
    # minC = deepcopy(C)
    # minC[0][0] = C[0][0]
    #
    # # for j in range(1, ysteps):
    # #     minC[0][j] = minC[0][j - 1] + C[0][j]
    # #
    # # for i in range(1, xsteps):
    # #     minC[i][0] = minC[i-1][0] + C[i][0]
    #
    # for i in range(1, xsteps):
    #     for j in range(1, ysteps):
    #         minC[i][j] = min(minC[i-1][j], minC[i][j-1]) + C[i][j]

def first(input):
    C = []

    c = {}

    for line in input.split("\n"):
        if ("A" in line) or ("B" in line):
            x, y = line.split(":")[1].strip().split(",")
            x = int(x.split("X")[1])
            y = int(y.split("Y")[1])
            is_a = "Button A" in line
            if is_a:
                c["A"] = {}
                c["A"]["x"] = x
                c["A"]["y"] = y
            else:
                c["B"] = {}
                c["B"]["x"] = x
                c["B"]["y"] = y

        if "Prize:" in line:
            px, py = line.split(":")[1].strip().split(",")
            px = int(px.split("=")[1])
            py = int(py.split("=")[1])
            c["P"] = {}
            c["P"]["x"] = px
            c["P"]["y"] = py
            C.append(Box(c))
            c = {}
    print()
    s = 0
    for cmd in C:
        s += solve(cmd)
    print(s)


def second(input):
    M = []

    for line in input.split("\n"):
        M.append(list(line.strip()))

    nrows, ncols = len(M), len(M[0])

if __name__ == "__main__":
    data = Path(f"day{day}.input").read_text()
    example = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
    #second(example)

    #second(data)
    first(data)
