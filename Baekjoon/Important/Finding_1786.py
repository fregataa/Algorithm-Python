t = input().strip("\n")
p = input().strip("\n")

n = len(t)
m = len(p)
fail = [0 for _ in range(m)]

j = 0
for i in range(1,m):
    while j > 0 and p[i] != p[j]:
        j = fail[j-1]
    if p[i] == p[j]:
        j += 1
        fail[i] = j

j = 0
answer_list = []
for i in range(n):
    while j > 0 and t[i] != p[j]:
        j = fail[j-1]
    if t[i] == p[j]:
        if j == m-1:
            answer_list.append(i-m+2)
            j = fail[j]
        else:
            j += 1

print(len(answer_list))
print(*answer_list)


# i, j = 0, 1
# while i<m:
#     if p[i] != p[j]:
#         i += fail[j]
#     else:
#         fail[i] += 1
#         j += 1
#     i += 1
# print(fail)

# i, j = 0, 0
# while i<n:
#     if t[i] != p[j]:
#         i += fail[j]
#     else:
#         if j != m-1:
#             j += 1 
#         else:
#             answer += 1
#             answer_list.append(i-j+1)
#             j = 0

#     i += 1
