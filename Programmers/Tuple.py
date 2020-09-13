import re
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

answer = []
# s = re.findall('\d+',s)
print(s)
s = re.findall('\d+[,0-9]*',s)
nums = list(map(lambda x: re.findall('\d+',x), s))

for tup in sorted(nums, key = lambda x: len(x)):
    for n in tup:
        if int(n) in answer:
            continue
        answer.append(int(n))

print(nums)
