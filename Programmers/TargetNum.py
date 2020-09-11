n = [1,1,1,1,1]
t = 3
ln = len(n)

def find(cnt: int, num: int):
    if cnt == ln:
        if num == t:
            return 1
        return 0
    return find(cnt+1, num+n[cnt]) + find(cnt+1, num-n[cnt])

print(find(0, 0))