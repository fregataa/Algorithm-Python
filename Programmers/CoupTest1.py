import sys
sys.setrecursionlimit(10**6)

def div(n,k):
    a=n//k
    b=n%k
    if not b:
        b=1
    if a<k:
        return a*b
    else:
        return div(a,k)*b


def solution(n):
    answer = [0,0]
    for i in range(9, 1,-1):
        num = div(n,i)
        if num > answer[1]:
            answer = [i, num]
    
    return answer

print(solution(14))