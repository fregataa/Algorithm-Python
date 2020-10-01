def solution(lines):
    answer = 0
    jobs = []
    timeline = []
    for line in lines:
        tmp = line.split()
        s = tmp[1].split(':')
        hour, minute, sec = map(float, s)
        t = float(tmp[2].strip('s'))
        end = (hour*3600 + minute*60 + sec)*1000
        start = end - t*1000 + 1
        jobs.append([start, end])
        d1 = {'left': end-999, 'right': end, 'count': 0}
        d2 = {'left': end, 'right': end+999, 'count': 0}
        timeline.append(d1)
        timeline.append(d2)
    for t in timeline:
        for i in range(len(jobs)):
            l, r =  jobs[i]
            if r < t['left'] or l > t['right']:
                continue
            t['count'] += 1
        answer = max(answer, t['count'])
    return answer

l =  [
'2016-09-15 01:00:04.002 2.0s',
'2016-09-15 01:00:07.000 2s'
]

print(solution(l))