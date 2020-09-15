n = int(input())
pic = [[x for x in list(map(int, list(input().rstrip('\n'))))] for _ in range(n)]

def find(p:list):
    flag = p[0][0]
    for i in range(len(p)):
        for j in range(len(p)):
            if flag == p[i][j]:
                continue
            h1 = p[:len(p)//2]
            h2 = p[len(p)//2:]
            return '('+find([x[:len(p)//2] for x in h1]) +find([x[len(p)//2:] for x in h1]) +find([x[:len(p)//2] for x in h2]) +find([x[len(p)//2:] for x in h2])+')'
    return str(flag)

print(find(pic))