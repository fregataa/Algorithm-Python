s = input()
for c in range(97, 123):
    print(s.find(chr(c)), end=' ')

# find() returns -1 when there is no item
# index() returns exception
# Plus, find() can only be used in String


# alp = [-1 for a in range(26)]
# for c in s:
#     alp[ord(c)-97] = s.index(c)
# for i in alp:
#     print(i, end=' ')


# alp = list('abcdefghijklmnopqrstuvwxyz')
# answer = []
# for c in alp:
#     if c in s:
#         answer.append(s.index(c))
#     else:
#         answer.append(-1)

# for i in answer:
#     print(i, end=' ')