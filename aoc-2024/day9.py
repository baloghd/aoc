day=9

from collections import Counter
from pathlib import Path

import numpy as np
from copy import deepcopy
from tqdm import tqdm
from itertools import chain, repeat, zip_longest
import networkx as nx



def first(input):
    e = ["." if i%2==1 else i//2 for i in range(1000000)]
    eidx = 0
    expanded = []
    dots = []
    for ch in input.strip():
        for _ in range(int(ch)):
            expanded.append(e[eidx])
        eidx = (eidx + 1) % len(e)

    #print(expanded)
    last_file_end_idx = 0
    for idx, d in enumerate(expanded):
        if d == ".":
            dots.append(idx)
        else:
            last_file_end_idx = idx
    #print(dots)

    expanded = list(expanded)

    pdot = 0
    pfile = last_file_end_idx

    while (dots[pdot] < len(expanded)) and (pfile >= 0):
        expanded[dots[pdot]] = expanded[pfile]
        expanded[pfile] = "."
        pfile -= 1
        while expanded[pfile] == ".":
            pfile -= 1
        pdot += 1
        if dots[pdot] > pfile: break


    #print("".join(expanded))
    s = 0
    for idx, v in enumerate(expanded):
        if v == ".": continue
        s += idx*int(v)
    print(s)


def get_file_empty_lists(expanded):
    file_list = []
    empty_space_list = []
    currfile = 0
    currfileidx = 0
    for idx, d in enumerate(expanded):
        if idx == len(expanded) - 1:
            if (currfile == "."):
                empty_space_list.append({
                    "fileid": currfile,
                    "length": idx - currfileidx,
                    "startpos": currfileidx
                })

            else:
                file_list.append({
                    "fileid": currfile,
                    "length": idx - currfileidx + 1,
                    "startpos": currfileidx
                })

        if d != currfile:
            if (currfile == "."):
                empty_space_list.append({
                    "fileid": currfile,
                    "length": idx - currfileidx,
                    "startpos": currfileidx
                })

            else:
                file_list.append({
                    "fileid": currfile,
                    "length": idx - currfileidx,
                    "startpos": currfileidx
                })

            currfile = d
            currfileidx = idx
    return file_list, empty_space_list

def place_to_leftmost_empty(expanded, file):
    E = deepcopy(expanded)
    in_empty = False
    empty_len = 0
    empty_idx = 0
    for idx, c in enumerate(expanded):
        if idx > file['startpos']: break
        if in_empty:
            if c == ".":
                empty_len += 1
            else:
                if empty_len >= file['length']:
                    #print(f"SUITABLE EMPTY SPACE FOUND for f{file['fileid']} @ {empty_idx}")
                    for j in range(empty_idx, empty_idx+file['length']):
                        E[j] = file['fileid']
                    for k in range(file['startpos'], file['startpos']+file['length']):
                        E[k] = "."
                    #print("".join(map(str, expanded)))
                    break
                in_empty = False
                empty_len = 0
        else:
            if c == ".":
                empty_idx = idx
                empty_len += 1
                in_empty = True
    return E





def second(input):
    e = ["." if i%2==1 else i//2 for i in range(1000000)]
    eidx = 0
    expanded = []

    for ch in input.strip():
        for _ in range(int(ch)):
            expanded.append(e[eidx])
        eidx = (eidx + 1) % len(e)

    file_list, empty_space_list = get_file_empty_lists(expanded)
    for idx, f in tqdm(enumerate(file_list[::-1])):
         expanded = place_to_leftmost_empty(expanded, f)
    #print("".join(map(str, expanded)))
    #
    #
    #
    # print("".join(map(str, expanded)))
    # file_list, empty_space_list = get_file_empty_lists(expanded)
    # print(file_list[::-1])
    #
    # for idx, f in enumerate(file_list[::-1]):
    #     #print(f"moving {f['fileid']}...")
    #     emptyspace = None
    #     emptyidx = 0
    #     #print(empty_space_list)
    #     for eidx, e in enumerate(empty_space_list):
    #         if f['length'] <= e['length']:
    #             #print(f"f{f['fileid']} -> idx{e['startpos']} ({eidx})")
    #             emptyspace = e
    #             emptyidx = eidx
    #             break
    #
    #     if emptyspace and emptyspace['startpos'] < f['startpos']:
    #
    #         # move file
    #         for i in range(
    #                 emptyspace['startpos'],
    #                 emptyspace['startpos']+f['length']
    #         ):
    #             expanded[i] = f['fileid']
    #
    #         # move empty
    #         for i in range(
    #                 f['startpos'],
    #                 f['startpos']+f['length']
    #         ):
    #             expanded[i] = "."
    #
    #         # merge new empty
    #
    #
    #         # create new empty from leftover space
    #         if f['length'] <= e['length']:
    #             empty_space_list[emptyidx]['startpos'] += e['length'] - f['length'] + 1
    #             empty_space_list[emptyidx]['length'] = e['length'] - f['length']
    #





        #print("".join(map(str, expanded)))
        #print("*"*30)
        #_, empty_space_list = get_file_empty_lists(expanded)

    s = 0
    for idx, v in enumerate(expanded):
        if v == ".": continue
        s += idx*int(v)
    print(s)


if __name__ == "__main__":
    data = Path(f"day{day}.input").read_text()
    example = """2333133121414131402"""
    #first(example)
    #first(data)

    # second(example)
    second(data)

# first
# 5595774106 too low
# second
# 8400763229943 too high
# 6282018255530 too low
