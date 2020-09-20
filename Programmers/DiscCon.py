import heapq as hq

def solution(jobs):
    n = len(jobs)
    time, end, q = 0,-1,[]
    cnt = 0
    
    answer = 0
    while cnt < n:
        for job in jobs:
            if end<job[0] <= time:
                answer += (time-job[0])
                hq.heappush(q, job[1])
        if len(q)>0:
            answer += len(q)*q[0]
            end = time
            time += hq.heappop(q)
            cnt += 1
        else:
            time += 1
    return answer // n

print(solution([[0,10], [2,1]]))


# import heapq as heapq

# def solution(jobs):
#     answer = 0
#     n = len(jobs)
#     cnt = 0
#     jobs = sorted(jobs, key = lambda x: (x[0], x[1]))
#     while jobs:
#         task_idx = 0
#         for i in range(len(jobs)):
#             if jobs[i][0] > cnt:
#                 break
#             if jobs[i][1] < jobs[task_idx][1]:
#                 task_idx = i
#         task = jobs.pop(task_idx)
#         cnt += task[1]
#         answer += cnt-task[0]
    
#     return answer//n