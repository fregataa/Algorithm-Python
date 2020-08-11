size = 10000
numbers = [i+1 for i in range(size)]
# numbers = set(range(1, 10000))

def finder(n: str):
    strNum = list(map(int, list(n)))
    newNum = int(n) + sum(strNum)
    if newNum > size or newNum not in numbers:
        pass
    else:
        numbers.remove(newNum)
        finder(str(newNum))
        
for i in numbers:
    finder(str(i))

for i in numbers:
    print(i)


def find(n):
    return n + sum(list(map(int, list(str(n)))))


# notSelfNum = []
# for i in range(size):
#     notSelfNum.append(i + sum(list(map(int, list(str(i))))))

# allNum = set(range(1, size))
# allNum = list(allNum - set(notSelfNum))
# allNum.sort()

# for i in allNum:
#     print(i)
