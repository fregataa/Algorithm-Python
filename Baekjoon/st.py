# n = int(input())

# allNum = [x+1 for x in range(n)]


a = [9,2,5,6,1,4,3,7,8]

b = list(map(lambda x: [x[0], x[1]], enumerate(a)))
print(b)

# for i in sorted(a)[0:3]:
#     print(i)



# for i in allNum:
#     print(i)

# l = [[0, 1, 2, 3, 4], ['4',2,0,1,0]]
# l[0][0] = int(l[1][0]) +1
# a = l[0][0]
# l[0][0] = -1
# print(l)
# print(a)


# visited = [[0]*4 for _ in range(6)]
# print(visited)
# visited[0][1] = -2
# print(visited)

# print('5\n1')

# for i in l:
#     print(i.count(0))

# N,M=map(int,input().split())
# M+=1
# a='2'.join(input()for i in range(N))+'2'*M
# print(a)
