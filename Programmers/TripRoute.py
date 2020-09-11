t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
# t = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]


# stck = [[["ICN"], t]]
# while stck:
#     # print(stck)
#     route, tckt = stck.pop()
#     if not tckt:
#         print(route)
#         break
#     node = route.pop()

#     l = []
#     for i in range(len(tckt)):
#         if tckt[i][0] == node:
#             newTickt = tckt[:]
#             newTickt.pop(i)
#             k = len(l) - 1
#             while k > -1 and l[k][0] < tckt[i][1]:
#                 k -= 1
#             l.insert(k+1, [tckt[i][1], newTickt])
    
#     for newNode, nTckt in l:
#         stck.append([route+[node, newNode], nTckt])



answer = ["ICN"]
chker = [True for _ in range(len(t))]

isEnd = False

def find(node):
    global isEnd
    if chker.count(True) == 0:
        isEnd = True
        return
    l = []
    for i in range(len(t)):
        if t[i][0] == node and chker[i]:
            k = len(l) - 1
            while k > -1 and l[k][1] > t[i][1]:
                k -= 1
            l.insert(k+1, [i, t[i][1]])
    for i, lv in l:
        chker[i] = False
        answer.append(lv)
        find(lv)
        if isEnd:
            return
        answer.pop()
        chker[i] = True

find("ICN")
print(answer)


# chker = [True for _ in range(len(t))]
# stck = ["ICN"]
# while stck:
#     node = stck.pop()
#     answer.append(node)
#     l = []
#     for i in range(len(t)):
#         if t[i][0] == node and chker[i]:
#             l.append(t[i][1])
#             chker[i] = False
#     if l:
#         stck += sorted(l, reverse=True)
#     else:
#         answer.pop()