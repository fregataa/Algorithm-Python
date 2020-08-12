import sys
line = ''.join(sys.stdin.readline().upper().split())
alp = [0 for a in range(26)]
for c in line:
    alp[ord(c) - 65] += 1
if alp.count(max(alp)) > 1:
    print('?')
else:
    print(chr(alp.index(max(alp)) + 65))

# we dont have to use sort. the code below can be faster

# alp = [0 for a in range(26)]
# for c in line:
#     if c == '\n':
#         break
#     if ord(c) > 90:
#         alp[ord(c)-97] += 1
#     else:
#         alp[ord(c)-65] += 1
# copyAlp = alp[:]
# copyAlp.remove(max(alp))
# if max(copyAlp) == max(alp):
#     print('?')
# else:
#     print(chr(alp.index(max(alp)) + 65))


# maxNum = 1
# flag = False
# for i in alp:
#     if i > maxNum:
#         maxNum = i
#         flag = False
#     elif i == maxNum:
#         flag = True

# if flag:
#     print('?')
# else:
#     print(chr( alp.index(max(alp)) + 65 ))