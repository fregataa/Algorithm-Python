tc = int(input())

for i in range(tc):
    line = list(map(int, input().split()))[1:]
    avg = sum(line) / len(line)
    bigger = len(list(filter(lambda x: x > avg, line)))
    print('{:.3f}%'.format(bigger/len(line)*100))