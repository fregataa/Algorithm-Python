# any의 발견 ㄷㄷ 

# def solution(pri, loca):
#     answer = 0
#     while True:
#         p = pri.pop(0)
#         loca -= 1
#         if pri and p < max(pri):
#             pri.append(p)
#             if loca < 0:
#                 loca = len(pri)-1
#             continue
#         answer+=1
#         if loca < 0:
#             return answer

def solution(pri, loca):
    q = list(enumerate(pri))
    answer = 0
    while True:
        job = q.pop(0)
        if q and any(job[1] < x[1] for x in q):
            q.append(job)
            continue
        answer += 1
        if job[0] == loca:
            return answer

pri = [2, 1, 3, 2]	
loca = 2
print(solution(pri, loca))