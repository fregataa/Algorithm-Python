N = int(input())
number = int(input())
nums = [[0]]
dp = {N: 0}

def find(cnt: int):
    if cnt > 8:
        return -1
    i = cnt-1
    l = []
    while i>0:
        a = nums[i]
        b = nums[cnt-i]
        for an in a:
            for bn in b:
                for r in [an+bn, an-bn, an*bn, an//bn]:
                    if r < 1 or r in l or r in dp:
                        continue
                    if r == number:
                        return cnt
                    dp[r] = 0
                    l.append(r)
        i-=1
    lastnum = int(str(N)*cnt)
    if lastnum == number:
        return cnt
    l.append(lastnum)

    # print(cnt,l)

    dp[lastnum] = 0
    nums.append(l)
    return find(cnt+1)

print(find(1))
