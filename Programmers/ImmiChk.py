n = 6
times = [7,10]

def solution(n, times):
    answer = 0
    lft, rgt = 1, n*times[0]
    while lft <= rgt:
        mid = (lft+rgt) >> 1
        cnt = sum([mid//t for t in times])
        if cnt < n:
            lft = mid+1
        else:
            rgt = mid-1
            answer= mid
    
    return answer

print(solution(n, times))