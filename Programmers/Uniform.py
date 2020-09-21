def solution(n, lost, reserve):
    r = len(reserve)
    for los in lost:
        for l in [los-1, los, los+1]:
            if l in reserve:
                reserve.remove(l)
                break
                
    return n-len(lost)+r-len(reserve)

n=5
lost = [1,2]
reserve = [2,3]

print(solution(n,lost,reserve))