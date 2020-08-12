t = 0
for c in input():
    n = (ord(c)-65)//3 + 3
    if c == 'S' or c == 'V' or c == 'Y' or c == 'Z':
        n -= 1
    t += n
print(t)