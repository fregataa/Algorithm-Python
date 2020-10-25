gears = []

for _ in range(4):
    gears.append(list(map(int, list(input().strip('\n')))))

k = int(input())
jobs = []
for _ in range(k):
    jobs.append(list(map(int, input().split())))
rot = []

def rotate(gear: list, direction: int):
    # print(gear, direction)
    if direction == 1:  # clock-wise
        gear.insert(0, gear.pop())
    else:   # anti clock-wise
        gear.append(gear.pop(0))
    # print(gear)

def send(idx: int, rot_dir: int, dir: int):
    if idx < 0 or idx > 3:
        return
    if dir == 1:    # right side
        if idx == 3 or gears[idx][2] == gears[idx+1][6]:
            return
        rot.append((idx+1, -(rot_dir)))
        send(idx+1, -(rot_dir), 1)
    else:   # left side
        if idx == 0 or gears[idx][6] == gears[idx-1][2]:
            return
        rot.append((idx-1, -(rot_dir)))
        send(idx-1, -(rot_dir), -1)

for gear, rot_dir in jobs:
    rot = [(gear-1, rot_dir)]
    send(gear-1, rot_dir, 1)
    send(gear-1, rot_dir, -1)
    # print(rot)
    for g, d in rot:
        rotate(gears[g], d)
    # print(gears)


answer = 0
for i in range(4):
    answer += gears[i][0]*(2**i)
print(answer)