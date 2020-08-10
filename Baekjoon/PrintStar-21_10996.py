n = int(input())

for i in range(n*2):
    if i%2 == 0:
        print("{0}{1}".format('* '*((n - 1)//2), '*') )
    else:
        print("{0}".format(' *'*(n//2)) )