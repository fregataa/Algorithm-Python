from collections import deque

visited = []
def checker(locations, board):
    checked_locations = []
    for l, r in locations:
        a = []
        if l[0] + l[1] < r[0]+r[1]:
            a = [[l[0], l[1]], [r[0], r[1]]]
        else:
            a = [[r[0],r[1]], [l[0], l[1]]]
        if board[1+l[0]][1+l[1]] or board[1+r[0]][1+r[1]] or a in visited:
            continue
        if l[0]+l[1] == len(board)*2-6 or r[0]+r[1] == len(board)*2-6:
            return [[-100]]
        checked_locations.append(a)
        visited.append(a)
    return checked_locations
    
def solution(board):
    answer = 0
    size = len(board)
    for i in range(size):
        board[i] = [1] + board[i] + [1]
    board = [[1 for _ in range(size+2)]] + board + [[1 for _ in range(size+2)]] 
    
    q = deque([[[0,0], [0,1]]])
    while q:
        l, r = q.popleft()
        new_locations =[]
        for a,b,c,d in [[-1,0,-1,0], [1,0,1,0],[0,-1,0,-1],[0,1,0,1]]:
            new_locations.append([[l[0]+a,l[1]+b], [r[0]+c,r[1]+d]])
        if l[0] == r[0]:    # 가로로 놓인 경우
            if not (board[1+l[0]-1][1+l[1]] or board[1+r[0]-1][1+r[1]]):  # 윗부분에 벽 없는 경우
                new_locations.append([[l[0],l[1]], [l[0]-1, l[1]]])
                new_locations.append([[r[0]-1,r[1]], [r[0], r[1]]])
            if not (board[1+l[0]+1][1+l[1]] or board[1+r[0]+1][1+r[1]]):    # 아래에 벽 없는 경우
                new_locations.append([[l[0],l[1]], [l[0]+1, l[1]]])
                new_locations.append([[r[0]+1,r[1]], [r[0], r[1]]])
        else:       # 세로로 놓인 경우
            if not (board[1+l[0]][1+l[1]-1] or board[1+r[0]][1+r[1]-1]):  # 왼쪽에 벽 없는 경우
                new_locations.append([[l[0],l[1]], [l[0], l[1]-1]])
                new_locations.append([[r[0],r[1]-1], [r[0], r[1]]])
            if not (board[1+l[0]][1+l[1]+1] or board[1+r[0]][1+r[1]+1]):
                new_locations.append([[l[0],l[1]], [l[0], l[1]+1]])
                new_locations.append([[r[0],r[1]+1], [r[0], r[1]]])
        print(new_locations)
        new_locations = checker(new_locations, board)
        print(new_locations)
        answer += 1
        if new_locations[0][0] == -100:
            return answer
        l = new_locations[:]
        q = deque(l)

b=[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(b))