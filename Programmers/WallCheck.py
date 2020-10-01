# def solution(n, weak, dist):
#     answer = 0
#     dist_weak = [0 for _ in range(len(weak))]
#     num_of_weak = len(weak)
#     temp = weak[:] + [weak[0]+n]
#     for i in range(len(weak)):
#         dist_weak[i] = temp[i+1] - temp[i]
#     for person in reversed(dist):
#         longest_way = 0
#         long_way = []
#         d = dist_weak + dist_weak + dist_weak
#         for i in range(len(dist_weak), len(dist_weak)*2):
#             m = 0
#             if  d[i] <= person:
#                 j=i
#                 l=[]
#                 while m+d[j] <= person:
#                     m += +d[j]
#                     l.append(j-len(dist_weak))
#                     j+=1
#                 if m+d[i-1]+d[j+1] > longest_way:
#                     long_way = l[:]
#                     longest_way = m+d[i-1]+d[j+1]
#         if not long_way:
#             continue
#         l = []
#         num_of_weak -= len(long_way)+1
#         answer += 1
#         if not num_of_weak:
#             return answer
#         for i in range(len(dist_weak)):
#             if i in long_way or i-1 in long_way or i+1 in long_way:
#                 continue
#             l.append(dist_weak[i])
#         dist_weak = l[:]
#     return -1


from collections import deque

def solution(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak])
    visited = set()
    visited.add(tuple(weak))
    for i in range(len(dist)):
        d = dist[i]
        for _ in range(len(q)):
            print(q)
            current = q.popleft()
            for p in current:
                l = p
                r = (p + d) % n
                if l < r:
                    temp = tuple(filter(lambda x: x < l or x > r, current))
                else:
                    temp = tuple(filter(lambda x: x < l and x > r, current))
                print('temp =',temp)
                if len(temp) == 0:
                    return (i + 1)
                elif temp not in visited:
                    visited.add(temp)
                    q.append(list(temp))
    return -1


n = 12
w = [1, 5, 6, 10]
d = [1, 2, 3, 4]
print(solution(n,w,d))