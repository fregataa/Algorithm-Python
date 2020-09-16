stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k =3

def solution(s, k):
    l = 1
    r = 200000000
    
    answer = 0
    while l<=r:
        mid = (l+r) >> 1
        chk = 0
        for stone in s:
            if stone < mid:
                chk += 1
                if chk >= k:
                    r = mid-1
                    chk = -1
                    break
            else:
                chk = 0
        if chk != -1:
            l = mid + 1
            answer = max(mid, answer)
    return answer

print(solution(stones,k))

# THIS PROBLEM IS NOT ABOUT DP

# s = [5]
# k=1

# def solution(s,k):
#     ls = len(s)
#     dp = [1 for _ in range(ls+1)]
#     mins = [0] + sorted(set(s))
#     minIdx = 1
#     answer = 0
#     while True:
#         if minIdx > len(mins)-1:
#             return answer
#         minv = mins[minIdx] - mins[minIdx-1]
#         answer += minv
#         for i in range(ls):
#             s[i] -= minv
#             if s[i]:
#                 continue
            
#             dp[i] = dp[i-1] + dp[i+1]
#             if dp[i] > k:
#                 return answer
#             dp[i+dp[i+1]-1] = dp[i]
#             dp[i-dp[i-1]+1] = dp[i]
#         minIdx += 1
    
# print(solution(s,k))