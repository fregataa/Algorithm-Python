import sys

# tc = int(sys.stdin.readline())
# for i in range(tc):
#     a, b = map(int, sys.stdin.readline().split())
#     result = "Case #"
#     result = result + str(i+1) + ": " + str(a+b)
#     print(result)

for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{0}:".format(i+1), a+b)