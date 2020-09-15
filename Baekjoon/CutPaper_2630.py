n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))
a = [0,0]

def divide(p: list):
    chk = p[0][0]
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i][j] == chk:
                continue
            h1 = p[:len(p)//2]
            h2 = p[len(p)//2:]
            divide([x[:len(p)//2] for x in h1])
            divide([x[len(p)//2:] for x in h1])
            divide([x[:len(p)//2] for x in h2])
            divide([x[len(p)//2:] for x in h2])
            return
    if chk:
        a[1] += 1
    else:
        a[0] += 1

divide(paper)
print(a[0])
print(a[1])
