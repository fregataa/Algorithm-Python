n,m = map(int, input().split())

graph = []
red, blue = [], []
for i in range(n):
    line = list(input().strip('\n'))
    graph.append(line)
    if 'R' in line:
        red = [i, line.index('R')]
    if 'B' in line:
        blue = [i, line.index('B')]

print(graph)
print(red, blue)

def move(first: list, second: list, dir: tuple):
    x,y = first
    a,b = second
    while 1:
        if graph[x][y] == 'O':
            x,y = -1,-1
            break
        if graph[x][y] == '#':
            x-= dir[0]
            y-= dir[1]
            break
        x+=dir[0]
        y+=dir[1]
    
    while 1:
        if graph[a][b] == 'O':
            a,b = -1,-1
            break
        if graph[a][b] == '#' or (a==x and b==y):
            a-=dir[0]
            b-=dir[1]
            break
        a+=dir[0]
        b+=dir[1]
        
    return [x,y], [a,b]

def chker(r,b,an):
    if b[0] == -1:
        return -1
    if r[0] == -1:
        return 0
    return (r,b,an)

answer = 0
q=[(red, blue, answer)]
while q:
    r, b, an = q.pop(0)
    if an > 10:
        continue
    an += 1
    if r[0] < b[0]:
        a, b = move(r,b, (-1,0))
        c, d = move(b,r, (1,0))
        x, y = chker(a,b,an), chker(d,c,an)
        if x == 0 or y == 0:
            print(an)
            exit()
        if x != -1:
            q.append(x)
        if y != -1:
            q.append(y)
    else:
        a,b=move(b,r, (-1,0))
        c,d=move(r,b, (1,0))
        x, y = chker(a,b,an), chker(d,c,an)
        if x == 0 or y == 0:
            print(an)
            exit()
        if x != -1:
            q.append(x)
        if y != -1:
            q.append(y)

    if r[1] < b[1]:
        a,b=move(r,b, (0,-1))
        c,d=move(b,r, (0,1))
        x, y = chker(a,b,an), chker(d,c,an)
        if x == 0 or y == 0:
            print(an)
            exit()
        if x != -1:
            q.append(x)
        if y != -1:
            q.append(y)
    else:
        a,b=move(b,r, (0,-1))
        c,d=move(r,b, (0,1))
        x, y = chker(a,b,an), chker(d,c,an)
        if x == 0 or y == 0:
            print(an)
            exit()
        if x != -1:
            q.append(x)
        if y != -1:
            q.append(y)

print(-1)