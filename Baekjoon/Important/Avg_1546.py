n = int(input())
score = list(map(int, input().split()))
m = max(score)

# newScore = [x/m*100 for x in score]
# print(sum(newScore)/n)

print( sum(list(map(lambda x: x/m*100, score)))/n )