n = int(input())

for i in range(n+1):
    if i==n:
        print(0)
        break
    if i + sum(list(map(int, list(str(i))))) == n:
        print(i)
        break

# print(list(list(str(n))))
# list(map(int, list(str(n))))
# print(n + sum(list(map(int, list(str(n))))))