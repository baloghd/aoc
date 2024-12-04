from collections import Counter
from pathlib import Path
import re

def first(input):
    left, right = [], []
    s=0
    for f in re.findall(r"mul\(\d+,\d+\)", input):
        print(f)
        q = 1
        for n in re.findall(r"(\d+)", f):
            q *= int(n)
        s += q
    #print(s)
    return s

def second(input):
    s=0

    # normals = []
    #
    # for do in input.split("don\'t()")[1:]:
    #     found = re.findall(r"(mul\(\d+,\d+\))+?", do)
    #     print(found)
    #     if found:
    #         normals.extend(found[1:])
    #
    # #print(normals)



    # until first do

    # for f in re.findall(r"don\'t\(\).(mul\(\d+,\d+\))+?", input):
    #     print(f)
    #     q = 1
    #     for n in re.findall(r"(\d+)", f):
    #         q *= int(n)
    #     s += q
    # print(s)

    dont_points = []
    do_points = []
    in_do = True
    last_change_idx = 0
    ss = 0
    for idx, char in enumerate(input[7:]):
        chunk = input[idx-7:idx]
        if in_do:
            if chunk == 'don\'t()':
                in_do = False
                print("do->don't")
                print(input[last_change_idx:idx])
                print('*'*60)
                ss += first(input[last_change_idx:idx])
                last_change_idx = idx
        else:
            if chunk.endswith("do()"):
                print("don't->do")
                in_do = True
                last_change_idx = idx

    #ss += first(input[last_change_idx:].split("do()")[-1])

    print(ss)

    # starting_do = True
    # if do_points[0] > dont_points[0]:
    #     starting_do = False

    # intervals = []
    # doidx, dontidx = 0, 0
    # curr = 0
    # label = ["do"]
    # if starting_do:
    #     intervals.append([0, do_points[0]])
    #     curr = do_points[0]
    #     doidx += 1
    #     label.append("do")
    # else:
    #     intervals.append([0, dont_points[0]])
    #     curr = dont_points[0]
    #     dont_points = dont_points[1:]
    #     dontidx += 1
    #     label.append("dont")
    #
    #
    # for i in range(max(len(do_points), len(dont_points))):
    #     if do_points[doidx] < dont_points[dontidx]:
    #         intervals.append([curr, do_points[doidx]])
    #         label.append("do")
    #         curr = do_points[doidx]
    #         if doidx < len(do_points):
    #             doidx += 1
    #     else:
    #         intervals.append([curr, dont_points[dontidx]])
    #         label.append("dont")
    #         curr = dont_points[dontidx]
    #         if dontidx < len(dont_points):
    #             dontidx += 1
    #
    # # the rest is the other
    # if doidx == len(do_points):
    #     intervals.append([curr, len(input)])
    #     label.append("do")
    # if dontidx == len(dont_points):
    #     intervals.append([curr, len(input)])
    #     label.append("dont")
    #
    # onlydo = []
    # for (start, end), command in zip(intervals, label):
    #     if command == "do":
    #         onlydo.append([start, end])
    #
    #
    #
    # ss = 0
    # for start, end in onlydo:
    #     ss += first(input[start:end])
    #     print(start, end)
    #     print(input[start:end])
    #     print(first(input[start:end]))
    # print(ss)


def dodont(do, dont):
    if do < dont:
        return "do"
    else:
        return "dont"



if __name__ == "__main__":
    data = Path("day3.input").read_text()
    print("".join(data))
    print(second(data))
    #first("{+*- #:/&mul(586,605)^':(mul(801,675)+!:*+do()where()why(239,64)/mul(975,879)mul(533,77)<@-?when()!who()mul(308,973)?)do())mul(449,426)~mul(200/%#$$)select()+:who()mul(463,285)',{#+&mul(821,317{]what()mul(964,348)*when()what()>([[mul(291,602)what(590,172)$}++';/mul(831,385){mul(299,25)mul(402,592)):what()]mul(49,44)/ &?~<mul(652,698):select()<#/! mul*{;,mul(338,76)- '@?<}who(826,950)-mul(499,44)>~,@$$)^%mul(21,890)}when()]+mul(696,311)<&when()when()/who()%^&mul(967,563)*@why(38,563){%{(mul(539,838)''&%)!mul(140,574)@mul(872,800)$$*[};?(mul(589,800)'[[<))'what()mul(571,216)+{!$!mul(327,56)}>@mul(179]{mul(728,336))who()*}/#from(385,957)mul(528,971)how(607,239)who()when()>mul(699,576),[where()-?;,mul(953,122why()from())-mul(50,327))&]select()*mul(191$<*}+*;%?~mul(717,832);!,-;#mul(877,863)})mul(10,865)how()>~mul(471,191)when()+;-,:#+>{mul(98,339) ,%%who()select()mul(590from()^,from(943,773)/%/(mul(498,29)+[-when()mul(556,808)$,{why()'who()what()}select()$mul(408,17)}@^}%what()when(533,550)mul(119,401)<&?select()!!],mul(800,82)~'++'-^'mul(202,735)'-;how()(why()-mul(878,380)++:,'%>select()why(),mul(517,67):(,mul(57,468)]!!?^who()'who()how()(mul(362,246){[select()@-,mul(790,848)who()/how()&;~mul(896,459)mul(244,758)^do()]*mul(393,498)how(827,483)++[;$^mul(242,357)?mul(246,74)mul(243,685)$-*how(); @;<!mul(22,701)from()-;<mul(362,732)%do()<</[select(247,938)select())]mul(560,346)@(-:/from()mul(149,424) mul(662,460)from(736,545);where()how()[mul(56,361)${&#^][%:;mul(804,220)'why())&+: [why()&mul(64,840)mul(689,477)mul(279,571):^how(543,315)who()mul(552,111)/+who()mul(422,133)&&;from()what();mul(394,845+]mul(317,924)!'mul(300,16where()from()[mul(86,484)$where()?who()(&what()-#)don't()")
    #second("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    #second("".join(data))


# 81134958 too low
# 96997035 too low
# 122519171 too high
# 122467457 ---
# 118173507

