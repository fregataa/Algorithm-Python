# Not a good problem..

import heapq as hq

def solution(ops):
    h = []
    for op in ops:
        inst = op.split()
        if inst[0] == "I":
            hq.heappush(h, int(inst[1]))
        elif inst[1] == "1":
            if not h:
                continue
            h.remove(hq.nlargest(1,h)[0])
        else:
            if not h:
                continue
            hq.heappop(h)
    if h:
        return [hq.nlargest(1,h)[0], hq.heappop(h)]
    else:
        return [0,0]