n = int(input())

for i in range(n*2 - 1):
    print( "{0}{1}*{1}".format(' '*(n-1-abs(n-1-i)), '*'*(abs(n-1-i)) ) )
