distance = 25
rocks = [2, 14, 11, 21, 17]
n=2

def solution(dist, rocks, n):
    if n == len(rocks):
        return distance     # 이런 test case는 애초에 안 넣어뒀다
    rocks = [0]+sorted(rocks)+[dist]
    lft, rgt = 1, dist
    answer = 0

    while lft <= rgt:
        mid = (lft+rgt) >> 1
        now = 0
        cnt = 0
        for i in range(1,len(rocks)):
            if rocks[i] - rocks[now] < mid:
                cnt += 1
                if cnt > n:
                    break
            else:
                now = i
        if cnt > n:
            rgt = mid - 1
        else:
            lft = mid + 1
            answer = max(answer, mid)
    return answer

print(solution(distance, rocks, n))