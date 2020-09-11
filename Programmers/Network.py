coms = [[1,1,0], [1,1,1], [0,0,1]]
n = len(coms)
answer = 0

# chk = [False for _ in range(n)]
for i in range(n):
    if coms[i][i] == 0:
        continue
    
    coms[i][i] = 0
    q = [i]
    while q:
        node = q.pop(0)
        for j in range(n):
            if coms[node][j] == 0 or coms[j][j] == 0:
                continue
            coms[j][j] = 0
            q.append(j)
    answer += 1

print(answer)



