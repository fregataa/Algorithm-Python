n = 5
ar1 = [9, 20, 28, 18, 11]
ar2 = [30, 1, 21, 17, 28]


def binary(iter, n1, n2):
    p = 1 << iter
    line = [' ' for _ in range(iter)]
    for i in range(iter):
        # print('n1 =',n1, 'n2 =',n2, 'p =',p)
        p = p >> 1
        if n1 // p < 1 and n2 // p < 1:
            continue
        line[i] = "#"
        n1, n2 = n1%p, n2%p
    
    return ''.join(line)

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(binary(n, arr1[i], arr2[i]))
    
    return answer

print(solution(n, ar1, ar2))