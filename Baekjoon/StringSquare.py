lines = []
while 1:
    lines.append(input().strip("\n"))
    if lines[-1] == ".":
        lines.pop()
        break

for a in range(len(lines)):
    answer = 0
    i=1
    iter_lim = len(lines[a]) // 2
    while i <= iter_lim:
        char = lines[a][:i]
        
        i+=1
