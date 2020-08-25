line = input().split('-')
minus = 0
for i in line[1:]:
    minus += sum(map(int, i.split('+')))
print(sum(map(int, line[0].split('+'))) - minus)