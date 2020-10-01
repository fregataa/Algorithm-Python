k = [[1, 1, 1], [1, 0, 0], [0, 1, 1]]
l=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def check(board, m,n):
    for i in range(n):
        for j in range(n):
            if board[m-1+i][m-1+j] != 1:
                return False
    return True

def putKey(a,b,key,board, flag):
    for i in range(len(key)):
        for j in range(len(key)):
            if flag:
                board[a+i][b+j] += key[i][j]
            else:
                board[a+i][b+j] -= key[i][j]

def rotate(k):
    return list(zip(*k[::-1]))

def solution(key, lock):
    if sum([x.count(1) for x in key]) < sum([x.count(0) for x in lock]):
        return False
    m, n = len(key), len(lock)

    board = [[0] * (m*2 + n-2) for _ in range(m*2+n-2)]
    
    for i in range(n):
        for j in range(n):
            board[m-1+i][m-1+j] = lock[i][j]

    rotated_key = key
    for i in range(m+n-1):
        for j in range(m+n-1):
            for _ in range(4):
                rotated_key = rotate(rotated_key)
                putKey(i,j,rotated_key, board, True)
                if check(board,m,n):
                    return True
                putKey(i,j,rotated_key,board, False)
    return False

print(solution(k,l))

# rots = []

# def rotate(k):
#     r = []
#     for a, b in k:
#         r.append([b,-a])
#     return r
    
# def check(k,l,n,m):
#     # chker = [x for x in zip(range(-n+1,m+n-1), range(-n+1,m+n-1))]
#     chker = []
#     for i in range(-n+1,m+n-1):
#         for j in range(-n+1,m+n-1):
#             chker.append([i,j])
#     # chker = list(map(lambda x,y: (x,y), [x for x in range(-n+1,m+n-1)], [x for x in range(-n+1,m+n-1)]))

#     print(chker)
#     for a,b in chker:
#         for _ in range(4):
#             k = rotate(k)
#             li = l[:]
#             flag = False
#             for k1, k2 in k:
#                 # print(li, k, a, b)
#                 if not (0<=k1+a<n and 0<=k2+b<n):
#                     continue
#                 if [k1+a, k2+b] not in li:
#                     flag = True
#                     break
#                 li.remove([k1+a, k2+b])
#             if flag:
#                 continue
#             if not li:
#                 return True
#     return False    
        
# def solution(key, lock):
#     if sum([x.count(1) for x in key]) < sum([x.count(0) for x in lock]):
#         return False
#     a, b = 0,0
#     loca = []
#     m = len(key[0])
#     for i in range(m):
#         for j in range(m):
#             if key[i][j]==0:
#                 continue
#             if a+b == 0:
#                 a,b = i,j
#             loca.append([i-a, j-b])
#     n = len(lock[0])
#     l = []
#     for i in range(n):
#         for j in range(n):
#             if lock[i][j]:
#                 continue
#             l.append([i,j])
#     return check(loca,l,n,m)
