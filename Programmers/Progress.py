pro = [95, 90, 99, 99, 80, 79]	
speed = [1, 1, 1, 1, 1, 1]

def solution(progress, speed):
    answer = []
    time = list(map(lambda x,y: -(x-100)//y, progress, speed))
    now = 0
    cnt = 1
    for i in range(1,len(time)):
        if time[now] < time[i]:
            answer.append(cnt)
            cnt = 1
            now = i
        else:
            cnt += 1
    answer.append(cnt)
    return answer

print(solution(pro, speed))
