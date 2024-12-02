from collections import Counter
from pathlib import Path



def safe(level):
    inc, dec = False, False
    for idx, l in enumerate(level):
        if idx == 0: continue
        if (level[idx-1] > l):
            dec = True
        if (level[idx-1] < l):
            inc = True

        if (level[idx-1] < l) and dec:
            return False
        if (level[idx-1] > l) and inc:
            return False
        if (abs(level[idx-1] - l) < 1) or (abs(level[idx-1] - l) > 3):
            return False
    return True

def first(input):
    lines = []

    for line in input.split("\n"):
        parsed = list(map(int, line.split()))
        lines.append(parsed)


    countsafe = 0
    for line in lines:
        le = len(line)
        issafe = safe(line)

        countsafe += int(issafe)

    print(countsafe)

def second(input):
    lines = []

    for line in input.split("\n"):
        parsed = list(map(int, line.split()))
        lines.append(parsed)


    countsafe = 0
    for line in lines:
        le = len(line)
        issafe = safe(line)
        couldbesafe = False
        for skip in range(0, le):
            skipped = line[:skip] + line[skip+1:]
            if safe(skipped):
                couldbesafe = True
        countsafe += int(issafe or couldbesafe)

    print(countsafe)


if __name__ == "__main__":
    data = Path("day2.input").read_text()
    first(data)
    second(data)


