user = 	["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned = ["*rodo", "*rodo", "******"]

allCom = []
result = []
def dfs(cnt: int, route: list):
    if cnt < 0:
        if set(route) not in result:
            result.append(set(route))
        return
    r = 0
    for num in allCom[cnt]:
        if num in route:
            continue
        dfs(cnt-1, route+[num])

for bID in banned:
    l = []
    for i in range(len(user)):
        if len(user[i]) != len(bID):
            continue
        flag = i
        for c1, c2 in zip(bID, user[i]):
            if c1 == '*':
                continue
            if c1 != c2:
                flag = -1
                break
        if flag != -1:
            l.append(flag)
    allCom.append(l)

# print(allCom)
dfs(len(allCom)-1, [])
answer = len(result)

print(answer)

