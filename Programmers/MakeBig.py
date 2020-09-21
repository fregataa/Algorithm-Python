def solution(number, k):
    answer = []
    num = list(map(int, list(number)))
    start=0
    for i in range(k+1):
        if num[i] > num[start]:
            start = i
    cnt = k-start
    print(start, cnt)
    for i in range(start,len(num)-1):
        if cnt and num[i] < num[i+1]:
            cnt -= 1
            continue
        answer.append(str(num[i]))
    answer.append(str(num.pop()))
    for i in range(cnt):
        answer.pop()
    return ''.join(answer)


n = "1231234"
k=3

print(solution(n,k))