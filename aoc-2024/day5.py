from collections import Counter
from pathlib import Path

import networkx
import numpy as np
from copy import deepcopy
import networkx as nx
day = 5
def first(input):

    rules = []
    updates = []
    isbefore = {}
    for line in input.split():
        if not line:
            continue

        if "|" in line:
            rules.append(line.split("|"))
        else:
            updates.append(line.split(","))

    G = networkx.DiGraph()
    G.add_edges_from(rules)

    for a, b in rules:
        if a not in isbefore:
            isbefore[a] = []
        isbefore[a].append(b)

    middlesum = 0
    for u in updates:
        if list(nx.topological_sort(G.subgraph(u))) == u:
            middlesum += int(u[len(u) // 2])
    print(middlesum)

def second(input):

    rules = []
    updates = []
    isbefore = {}
    for line in input.split():
        if not line:
            continue

        if "|" in line:
            rules.append(line.split("|"))
        else:
            updates.append(line.split(","))

    G = networkx.DiGraph()
    G.add_edges_from(rules)

    for a, b in rules:
        if a not in isbefore:
            isbefore[a] = []
        isbefore[a].append(b)

    corrected = 0
    for u in updates:
        correct = list(nx.topological_sort(G.subgraph(u)))
        if correct == u:
            pass
        else:
            corrected += int(correct[len(correct) // 2])
    print(corrected)


if __name__ == "__main__":
    data  = Path(f"day{day}.input").read_text()
    example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    first(data)
    second(data)