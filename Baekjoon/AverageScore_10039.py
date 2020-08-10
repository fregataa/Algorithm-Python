agg = 0
for i in range(5):
    score = int(input())
    if int(score) < 40:
        agg += 40
    else:
        agg += int(score)

print(agg//5)