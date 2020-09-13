board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

answer = 0
vssl = [-1]
for m in moves:
    for h in board:
        if not h[m-1]:
            continue
        pick = h[m-1]
        h[m-1] = 0

        if vssl[len(vssl)-1] == pick:
            vssl.pop()
            answer += 2
        else:
            vssl.append(pick)
        break

print(answer)

# answer = 0
# vssl = [-1]
# for m in moves:
#     if not board[m-1]:
#         continue
#     pick = board[m-1].pop()
#     if not pick:
#         continue
#     if vssl[len(vssl)-1] == pick:
#         answer += 2
#         vssl.pop()
#     else:
#         vssl.append(pick)