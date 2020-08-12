a, b = map(list, input().split())
m = int(''.join(reversed(a)))
n = int(''.join(reversed(b)))
if m > n:
    print(m)
else:
    print(n)