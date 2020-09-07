from collections import deque

prices = [1,2,3,2,3]

answer = []

for idx in range(len(prices)):
    for jdx in range(idx, len(prices)):
        if prices[idx] > prices[jdx] or jdx == len(prices) - 1:
            answer.append(jdx-idx)
            break

print(answer)



# for _ in range(len(prices)):
#     n = d.popleft()
#     l.append(n)
#     answer.append(-1)
#     for i, v in enumerate(l):
#         if l[i] == -1:
#             continue
#         answer[i] += 1
#         if v > n:
#             l[i] = -1