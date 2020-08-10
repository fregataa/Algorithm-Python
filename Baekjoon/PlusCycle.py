n = int(input())
origin = n
result = 0

while 1:
    a = int(n)//10
    b = int(n)%10
    c = a + b
    a = b
    b = c%10
    n = a*10 + b
    result += 1

    if origin == n:
        break

print(result)