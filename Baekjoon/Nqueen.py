n = int(input())
answer = 0

def find(vert: list, diag: list, pos: int):
    nl=vert[:]
    nl.append(pos)
    if len(nl)==n:
        global answer
        answer += 1
        return
    ndiag = list(map(lambda x: x[1]+1 if x[0]%2 else x[1]-1, enumerate(diag)))
    ndiag.append(pos-1)
    ndiag.append(pos+1)
    for i in range(n):
        if i in nl or i in ndiag:
            continue
        find(nl, ndiag, i)

for i in range(n):
    find([], [], i)

print(answer)