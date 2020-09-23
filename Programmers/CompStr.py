def solution(s):
    answer = 1000
    lnth = len(s)
    cand = []
    for i in range(1, lnth//2+1):
        cand += [i]
    cand.append(lnth)
        
    for i in cand:
        a = s[0:i]
        cnt = 0
        comp = ''
        for j in range(0,lnth,i):
            if j+i<=lnth and a == s[j:j+i]:
                cnt+=1
            else:
                if cnt>1:
                    comp += str(cnt)
                cnt = 1
                comp += a
                a = s[j:j+i]
        if cnt>1:
            comp += str(cnt)+a
        else:
            comp += a
        answer = min(answer, len(comp))
    return answer

