import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
nodes = [[0 for i in range(n+1)] for i in range(n+1)]
track = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a][b] = 1
    nodes[b][a] = 1


def dfs(current_node: int):
    current_link = nodes[current_node]
    for i, iv in enumerate(current_link):
        if iv and i not in track:
            track.append(i)
            dfs(i)

def bfs():
    q = [1]
    while len(q):
        current_node = q.pop(0)
        for i, iv in enumerate(nodes[current_node]):
            if iv and i not in track:
                track.append(i)
                q.append(i)    

dfs(1)
print(len(track)-1)

            