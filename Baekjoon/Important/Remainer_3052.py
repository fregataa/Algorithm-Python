num = []
for i in range(10):
    num.append(int(input())%42)

num = list(set(num))
print(len(num))