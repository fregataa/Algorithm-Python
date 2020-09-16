room_number=[1,3,4,1,3,1]
k=10

import sys
sys.setrecursionlimit(10000000)

def find(d: dict, num: int):
    if num not in d:
        d[num] = num+1
        return num
    empty = find(d, d[num])
    d[num] = empty+1
    return empty
        
def solution(k, rooms):
    answer = []
    d = dict()
    for r in rooms:
        answer.append(find(d, r))

    return answer

print(solution(k, room_number))

# THIS CODE is too slow.
# def find(d: dict, num: int):
#     if num not in d:
#         d[num] = num+1
#         return num
#     return find(d, d[num])


    # for r in room:
    #     if allroom[r]:
    #         # 방이 이미 찬 경우
    #         lt, rt = r, k
    #         while lt<=rt:
    #             mid = (lt+rt)>>1
    #     else:
    #         # 방이 빈 경우
    #         answer.append(r)