from collections import Counter
from pathlib import Path


def first(input):
    left, right = [], []

    for line in input.split("\n"):
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    d = 0
    for l, r in zip(left, right):
        d += abs(l-r)
    print(d)

def second(input):
    left, right = [], []

    for line in input.split("\n"):
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    rc = Counter(right)

    sim = 0
    for l in left:
        if l in rc:
            sim += rc[l] * l
    print(sim)


if __name__ == "__main__":
    data = Path("day1.input").read_text()
    first(data)
    second(data)


