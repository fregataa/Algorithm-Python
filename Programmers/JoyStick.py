def solution(name):
    isLeft = True
    cursor = 1
    idx = 0
    num_alp = 26
    answer = 0
    base = ['A' for _ in range(len(name))]

    if name == ''.join(base):
        return 0

    while name[idx + cursor] == 'A' and name[idx - cursor] == 'A':
        cursor += 1
    
    if name[idx + cursor] != 'A':
        isLeft = False
    
    while 1:

        idx %= len(name)
        if name[idx] != base[idx]:
            base[idx] = name[idx]
            mv = ord(name[idx]) - 65
            if mv > num_alp//2:
                answer += num_alp - mv
            else:
                answer += mv

        if name == ''.join(base):
            return answer

        if isLeft:
            idx -= cursor
            answer += cursor
        else:
            idx += cursor
            answer += cursor

        cursor = 1
    

print(solution("ABABAAAAABA"))



# def solution(name):
#     cnt = [min(26 - ord(i) + 65, ord(i) - 65) for i in name if i != 'A']
#     idx = [i for i, v in enumerate(name) if v != 'A']

#     graph = [idx[i + 1] - idx[i] for i in range(len(idx) - 1)] + [len(name) - idx[-1]]
#     if name[0] == 'A':
#         idx = [0] + idx
#         graph = [idx[1]] + graph

#     answer = [2 * sum(graph[:i]) + (len(name) - idx[i + 1]) for i, v in enumerate(idx) if 0 < v < len(name) // 2] + [
#         idx[-1], len(name) - idx[1]]
#     return sum(cnt) + min(answer)
