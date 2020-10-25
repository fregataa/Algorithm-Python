n, l = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def checker(line, l):
    for i in range(len(line)-1):
        if line[i] == line[i+1] or line[i] == -1:
            if i == len(line) - 2:
                return 1
            continue

        if line[i] > line[i+1]: # 내리막
            if line[i] - line[i+1] > 1:
                return 0
            edge = i+l
            if edge == len(line) -1:
                return 1
            if edge > len(line)-1 or line[i+1] != line[edge+1] or line[i+1:edge+1].count(line[i]) != l:
                return 0
        else:   # 오르막
            if line[i+1] - line[i] > 1:
                return 0
            edge = i-l+1
            if edge<0 or line[edge:i+1].count(line[i]) != l:
                return 0
    return 1
        
graph_90 =  list(zip(*graph[::-1]))
print(graph_90)
answer = 0

# print(graph)
for line in graph:
    answer += checker(line, l)
# print(graph)

for line in graph_90:
    list_line = list(line)
    answer += checker(list_line, l)

print(answer)