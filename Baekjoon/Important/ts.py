import sys

# def find(x: int, y: int, checker: list, board: list, color: int, footprints: list):
#     # find all ways recursively
#     max_trail = []
    
#     for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
#         if i+4*j not in checker and 0 <= i < 4 and 0 <= j < 4 and board[i][j]==color:
#             footprints.append(i+4*j)
#             returned_trail = find(i, j, checker + [i+4*j], 
#                                   board, color, footprints)
#             if len(returned_trail) > len(max_trail):
#                 max_trail = returned_trail
                
#     print("max trail :", *max_trail)
#     print("checker :", *checker)
    
#     if max_trail:
#         return max_trail
#     else:
#         return checker
        

# def solution(board):
#     sys.setrecursionlimit(10**6)
    
#     max_len = 0
#     trail_list = []
#     footprints = []
#     for i in range(4):
#         for j in range(4):
#             # if i+4*j in footprints:
#             #     continue
#             trail_checker = [i+4*j]
#             trail_list = find(i, j, trail_checker, board, board[i][j], footprints)
#             if max_len < len(trail_list):
#                 max_len = len(trail_list)
#     print("final trail list :", *trail_list)

#     if max_len == 1:
#         return -1
#     else:
#         return max_len

a = [0,1,2]
a = [a] + [[0 for _ in range(3)] for _ in range(2)]
print(a)