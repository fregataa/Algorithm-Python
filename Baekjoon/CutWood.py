from collections import Counter
n, m = map(int, input().split())

woods = sorted(Counter(map(int, input().split())).items(), reverse=True)
left, right = 1, woods[0][0]
answer = 0

while left <= right:
    mid = (left+right)>>1
    h = 0
    for x,y in woods:
        if x <= mid:
            break
        h += y*(x-mid)
    
    if h < m:
        right = mid - 1
    else:
        left = mid + 1
        answer = max(answer, mid)

print(answer)


# woods = list(map(int, sys.stdin.readline().split()))

# left, right = 0, max(woods) + 1
# while left <= right:
#     mid = (left + right) >> 1
#     r = 0
#     r = sum([w - mid for w in woods if w > mid])
            
#     if r < m:
#         right = mid
#     else:
#         if left == mid:
#             print(mid)
#             break
#         left = mid
