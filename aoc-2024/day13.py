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
from sympy.solvers.diophantine import diophantine
from sympy.abc import a,b
from sympy import symbols, Eq, solve
from sympy.parsing.sympy_parser import parse_expr
from scipy.optimize import milp, LinearConstraint
from scipy.sparse import csc_matrix
def msolve(c):
    TT = 10000000000000
    A_eq = csc_matrix([[c.A.x, c.B.x], [c.A.y, c.B.y]])
    b_eq = np.array([c.P.x + TT, c.P.y + TT])
    cc = [0, 0]
    constraints = LinearConstraint(A_eq, b_eq, b_eq)
    res = milp(c=cc, constraints=constraints, integrality=[3, 3], options={'presolve':False} )

    if res.success:
        x, y = res.x
        return int(x), int(y)
    else:
        return 0, 0
    # # c.A, c.B
    # #t_0 = symbols('t_0')
    # x = symbols('x')
    # TT = 10000000000000
    # dx = diophantine((c.A.x*a) + (c.B.x*b) - (c.P.x + TT))
    # dy = diophantine((c.A.y * a) + (c.B.y * b) - (c.P.y + TT))
    #
    # sols_x = list(dx)
    # sols_y = list(dy)
    # print(sols_x, sols_y)
    #
    # if len(sols_x) > 0:
    #     ax, ay = sols_x[0]
    #
    #     aeq = Eq(
    #         parse_expr(str(ax).replace("t_0", "x")),
    #         parse_expr(str(ay).replace("t_0", "x"))
    #     )
    #
    #     aeqs = solve(aeq, x)
    #
    #     if len(aeqs) > 0:
    #         A = int(aeqs[0])
    #
    #     aa = parse_expr(str(ay).replace("t_0", "x")).subs("x", A)
    #     print(aa)
    # else:
    #     aa = 0
    #
    # if len(sols_y) > 0:
    #     bx, by = sols_y[0]
    #
    #     beq = Eq(
    #         parse_expr(str(bx).replace("t_0", "x")),
    #         parse_expr(str(by).replace("t_0", "x"))
    #     )
    #
    #     beqs = solve(beq, x)
    #
    #     if len(beqs) > 0:
    #         B = int(beqs[0])
    #
    #
    #     bb = parse_expr(str(bx).replace("t_0", "x")).subs("x", B)
    #     print(bb)
    # else:
    #     bb = 0
    #
    # print("*"*62)
    # return aa, bb

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

    s = 0
    for cmd in C:
        a, b = msolve(cmd)
        s += (3*a + b)

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

# 2
# 133212165498122 too high
#  62613705485587 too low
#  61411131111473 too low