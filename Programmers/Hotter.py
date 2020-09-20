import heapq
from collections import deque

def solution(sco, k):
    heap = []
    for num in sco:
        heapq.heappush(heap, num)
    
    answer = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap)<<1)
        except IndexError:
            return -1
        answer += 1
    return answer

# without heapq
# def solution(sco, K):
#     mix = deque()
#     answer = 0
#     sco = deque(sorted(sco))

#     while sco and sco[0] < K:
#         s1 = 0
#         if mix:
#             s1 = mix.popleft()
#         else:
#             s1 = sco.popleft()
#         s2 = sco.popleft()
#         mix.append((max(s1,s2)<<1 + min(s1,s2)))
#         answer += 1
    


# Needs heapq !!!

# def solution(sco, K):
#     answer = 0
#     sco = deque(sorted(sco))
#     while len(sco) > 1 and (sco[0] < K or sco[1] < K):
#         s = sco.popleft()
#         if s < sco[0]:   
#             sco[0] += sco[0] + s
#         else:
#             sco[0] += s<<1
#         answer += 1
#     if sco[0] < K:
#         return -1
#     return answer