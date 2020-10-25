def solution(n, t, m, timetable):
    times = sorted(list(map(lambda x: (int(x.split(':')[0]), int(x.split(':')[1])), timetable)), key=lambda x: (x[0], x[1]))
    bus = 9*60
    last = 0
    timeIdx = 0

    while n:
        if timeIdx == len(times):
            last = bus+1
            bus += t
            n -= 1
            continue
        t1, t2 = times[timeIdx]
        space = m
        while space and timeIdx<len(times) and t1*60+t2<= bus:
            timeIdx += 1
            space -= 1
            if timeIdx < len(times):
                t1, t2 = times[timeIdx]
        if space:
            last = bus + 1
        else:
            last = t1*60 + t2
        n -= 1
        bus += t
        

    last -= 1
    answer = str(format(last//60,'02')) + ':'+str(format(last%60,'02'))
    return answer


n = 3
t = 5
m = 4
timetable = ["09:00", "09:00",]
print(solution(n,t,m,timetable))