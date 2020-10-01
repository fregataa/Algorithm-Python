def check_p(wall_p,wall_b, i, j):
    if i==0 or wall_p[i-1][j] or (j>0 and wall_b[i][j-1]) or wall_b[i][j]:
        return True
    return False

def check_b(wall_p, wall_b, i, j):
    if i>0 and (wall_p[i-1][j] or wall_p[i-1][j+1] or (j>0 and wall_b[i][j-1] and wall_b[i][j+1])):
        return True
    return False

def check_all(wall_p, wall_b):
    for i in range(len(wall_p)):
        for j in range(len(wall_p[0])):
            if (wall_p[i][j] and not check_p(wall_p, wall_b,i,j)) or (wall_b[i][j] and not check_b(wall_p, wall_b,i,j)):
                return False
    return True
    
def solution(n, build_frame):
    answer = []
    wall_p = [[0 for _ in range(n+2)] for _ in range(n+1)]    # 기둥 맵
    wall_b = [[0 for _ in range(n+2)] for _ in range(n+1)]    # 보 맵
    for y,x,a,b in build_frame:
        if b:   # 설치
            if a==0:   # 기둥
                if check_p(wall_p, wall_b,x,y):
                    wall_p[x][y] = 1
            else:   # 보
                if check_b(wall_p,wall_b,x,y):
                    wall_b[x][y] = 1
        else: # 삭제
            if a==0:    # 기둥
                wall_p[x][y] = 0
                if not check_all(wall_p, wall_b):
                    wall_p[x][y] = 1
            else:   # 보
                wall_b[x][y] = 0
                if not check_all(wall_p, wall_b):
                    wall_b[x][y] = 1
    for i in range(len(wall_p)):
        for j in range(len(wall_p[0])):
            if wall_p[i][j]:
                answer.append([j,i,0])
            if wall_b[i][j]:
                answer.append([j,i,1])
    print(wall_p)
    print(wall_b)
    return sorted(answer, key=lambda x: (x[0],x[1],x[2]))


n=5
b = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,b))