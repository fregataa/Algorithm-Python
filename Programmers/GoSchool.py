p = [[4,2]]
m = 5
n = 2

nodes = [[0 for _ in range(m)] + [-1] for _ in range(n)] + [[-1 for _ in range(m+1)]]
for x,y in p:
    nodes[x-1][y-1] = -1
nodes[0][0] = 1

for i in range(n):
    for j in range(m):
        if nodes[i][j] == -1:
            continue
        for x,y in [(i+1, j), (i, j+1)]:
            if nodes[x][y] == -1:
                continue
            nodes[x][y] += nodes[i][j]

answer = nodes[n-1][m-1] % 1000000007
print(nodes)