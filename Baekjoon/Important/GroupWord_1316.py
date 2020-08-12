import sys
answer = 0
for i in range(int(input())):
    line = sys.stdin.readline()
    if list(line) == sorted(line, key = line.find):
        answer += 1
print(answer)


# n = int(input())
# answer = 0
# while n > 0:
#     line = sys.stdin.readline()
#     line = re.sub(r'([a-z])\1+', r'\1', line)
#     for c in line:
#         if line.count(c) > 1:
#             break
#         if line.find(c) == len(line) - 1:
#             answer += 1
#             break
#     n -= 1
# print(answer)


# while n > 0:
#     line = sys.stdin.readline()
#     alp = {}
#     for c in line:
#         if line.find(c) == len(line) - 1:
#             answer += 1
#             break
#         if c in alp.keys():
#             if line.find(c) - alp[c] > 1:
#                 break
#             else:
#                 alp[c] = line.find(c)
#                 line = line.replace(c, '.', 1)
#         else:
#             alp[c] = line.find(c)
#             line = line.replace(c, '.', 1)
#     n -= 1
# print(answer)
