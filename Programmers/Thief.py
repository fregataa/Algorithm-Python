money = [1,2,3,1]

dp1 = []
dp2 = []
dp1.append(money[0])
dp1.append(max(money[1], dp1[0]))
dp2.append(money[-1])
dp2.append(max(money[-2], dp2[0]))
for i in range(2, len(money)):
    dp1.append(max(dp1[i-2]+money[i], dp1[i-1]))
    dp2.append(max(dp2[i-2]+money[-1-i], dp2[i-1]))

answer = max(dp1[-2], dp2[-2])

print(answer)