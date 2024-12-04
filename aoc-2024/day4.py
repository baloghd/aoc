from collections import Counter
from pathlib import Path
import numpy as np
from copy import deepcopy

# diagonal

# written backwards
# overlapping



def first(input):
    M = []

    for line in input.split("\n"):
        M.append(list(line.strip()))

    nrows, ncols = len(M), len(M[0])

    npM = np.array(M)
    Mford_hor = np.fliplr(npM)
    Mford_ver = np.flipud(npM)

    count = 0
    # horizontal
    for i in range(nrows):
        for j in range(ncols):
            if (j <= ncols - 4) and (list("XMAS") == [M[i][j+x] for x in range(4)]):
                count += 1

    # written backwards
    for i in range(nrows):
        for j in range(ncols):
            if (j <= ncols - 4) and (list("XMAS") == [Mford_hor[i][j+x] for x in range(4)]):
                count += 1


    # vertical
    for i in range(nrows):
        for j in range(ncols):
            if (i <= nrows - 4) and (list("XMAS") == [M[i+x][j] for x in range(4)]):
                count += 1
    # written backwards
    for i in range(nrows):
        for j in range(ncols):
            if (i <= nrows - 4) and (list("XMAS") == [Mford_ver[i+x][j] for x in range(4)]):
                count += 1

    # diagonal
    for k in [0,1,2,3]:
        Mford_diag = np.rot90(M, k=k)
        # for i in range(nrows):
        #     for j in range(ncols):
        #         if (i <= nrows - 4) and (j <= ncols - 4) and (list("XMAS") == [M[i+x][j+x] for x in range(4)]):
        #             count += 1
        # written backwards
        for i in range(nrows):
            for j in range(ncols):
                if (i <= nrows - 4) and (j <= ncols - 4) and (list("XMAS") == [Mford_diag[i+x][j+x] for x in range(4)]):
                    count += 1


    print(count)


def second(input):
    M = []

    for line in input.split("\n"):
        M.append(list(line.strip()))

    nrows, ncols = len(M), len(M[0])

    npM = np.array(M)
    count = 0
    for i in range(1, nrows-1):
        for j in range(1, ncols-1):
            if M[i][j] == "A" and ("".join([M[i-1][j-1], M[i][j], M[i+1][j+1]]) in {"MAS", "SAM"}) and ("".join([M[i+1][j-1], M[i][j], M[i-1][j+1]]) in {"MAS", "SAM"}):
                count += 1
                print(f"{i,j} found")
    print(count)




if __name__ == "__main__":
    data = Path("day4.input").read_text()
    example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

    example2 = """....XMAS
    XMASXMAS"""
    first(data)
    second(data)


# 3866 too high