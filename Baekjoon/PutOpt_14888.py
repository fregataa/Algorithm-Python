import math

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
max = -1000000000
min = 1000000000

def find(cnt: int, renum: int):
    for i in range(4):
        if ops[i]:
            re = renum
            if i==0:
                re += nums[cnt]
            elif i==1:
                re -= nums[cnt]
            elif i==2:
                re *= nums[cnt]
            else:
                if re > 0:
                    re //= nums[cnt]
                else:
                    re = math.trunc(re/nums[cnt])
            if cnt == n - 1:
                global max, min
                if max < re:
                    max = re
                if min > re:
                    min = re
                return
            ops[i] -= 1
            find(cnt+1, re)
            ops[i] += 1

find(1, nums[0])
print(max)
print(min)
