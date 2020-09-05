## Only by Pypy3

import sys
su = []
hline = [[False for _ in range(10)] for _ in range(9)]
vline = [[False for _ in range(10)] for _ in range(9)]
box = [[False for _ in range(10)] for _ in range(9)]

for i in range(9):
    l = list(map(int, sys.stdin.readline().split()))
    su.append(l)
    for li, lv in enumerate(l):
        hline[i][lv] = True
        vline[li][lv] = True
        box[(i//3)*3+li//3][lv] = True

def find(c: int):
    if c == 9 or (c == 8 and 0 not in su[c]):
        for i in range(9):
            print(*su[i])
        exit()
    if 0 in su[c]:
        zidx = su[c].index(0)
        cand = [x for x in range(1,10)]
        for i in range(1,10):
            if box[(c//3)*3 + (zidx//3)][i]:
                cand[i-1] = 0
            if vline[zidx][i]:
                cand[i-1] = 0
            if hline[c][i]:
                cand[i-1] = 0
        
        for cv in cand:
            if cv:
                su[c][zidx] = cv
                box[(c//3)*3 + (zidx//3)][cv] = True
                vline[zidx][cv] = True
                hline[c][cv] = True
                if 0 in su[c]:
                    find(c)
                else:
                    find(c+1)
                su[c][zidx] = 0
                box[(c//3)*3 + (zidx//3)][cv] = False
                vline[zidx][cv] = False
                hline[c][cv] = False
        return
            
    else:
        find(c+1)

find(0)