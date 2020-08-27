import sys
n,m,v = map(int, input().split())
nodes = {}

def dfs(current_node: int, chklist: list):
    chklist.append(current_node)
    print(current_node, end=' ')
    node_link = nodes[current_node]
    for i, iv in enumerate(node_link):
        if iv and i not in chklist :
            dfs(i, chklist)
    

def bfs(start: int):
    track = [start]
    queue = []
    queue.append(start)
    while len(queue) > 0:
        current_node = queue.pop(0)
        print(current_node, end=' ')
        node_link = nodes[current_node]
        for i, iv in enumerate(node_link):
            if iv and i not in track:
                track.append(i)
                queue.append(i)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a not in nodes:
        nodes[a] = [0 for i in range(n+1)]    
    nodes[a][b] = 1

    if b not in nodes:
        nodes[b] = [0 for i in range(n+1)]
    nodes[b][a] = 1
    
if v not in nodes:
    nodes[v] = []

dfs(v, [])
print()
bfs(v)

# DFS
# stack.append(v)
# while len(stack) > 0:
#     k = stack.pop()
#     pidx = len(stack)
#     if k not in track:
#         track.append(k)
#     for i, iv in enumerate(nodes[k-1]):
#         if iv:
#             stack.insert(pidx, i+1)
#             nodes[i][k-1] = 0
