num = []
for i in range(9):
    num.append(int(input()))
m = max(num)
print(m)
print(num.index(m)+1)
