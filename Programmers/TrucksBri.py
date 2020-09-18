from collections import deque

def solution(blen, weight, trucks):
    answer = 0
    tw = deque(trucks)
    on = deque()
    time = 0
    w = 0

    while tw or on:
        if tw and tw[0]+w <= weight:
            t = tw.popleft()
            w += t
            on.append([t, time])
        if on[0][1] + blen == time+1:
            a = on.popleft()
            w -= a[0]
        time += 1

    return time+1

b = 2
weight = 10
tw = [7,4,5,6]

print(solution(b, weight, tw))

# from collections import deque

# def solution(bridge_length, weight, tw):
#     answer = 1
#     time = bridge_length
#     bri = deque([0 for _ in range(bridge_length-1)] + [tw.pop(0)])
#     while True:
#         bri.popleft()
#         answer += 1
#         if sum(bri) == 0 and not tw:
#             break
#         if not tw:
#             continue
#         if sum(bri) + tw[0] > weight:
#             bri.append(0)
#             continue
#         bri.append(tw.pop(0))
#     return answer    