import sys
n = int(input())
nodemap = []
apart = []
apa_num = 0

for i in range(n):
    nodemap.append(list(sys.stdin.readline()))

def find(posX: int, posY: int, an: int):
    if int(nodemap[posX][posY]) == 1:
        nodemap[posX][posY] = 0
        if len(apart) > an:
            apart[an] += 1
        else:
            apart.append(1)

        if posX > 0:
            find(posX-1, posY, an)
        if posX < n-1:
            find(posX+1, posY, an)
        if posY > 0:
            find(posX, posY-1, an)
        if posY < n-1:
            find(posX, posY+1, an)

for i in range(n):
    for j in range(n):
        if int(nodemap[i][j]) == 1:
            find(i, j, apa_num)
            apa_num += 1

print(len(apart))
for i in sorted(apart):
    print(i)
# print(apart)