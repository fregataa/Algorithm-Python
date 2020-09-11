g = ["classic", "pop", "classic", "classic", "pop"]
p = [500,600,150,800,2500]

gp = []
d = {}
for i in range(len(g)):
    if g[i] in d:
        d[g[i]][0] += p[i]
    else:
        d[g[i]] = [p[i], 0]

for i in range(len(g)):
    gp.append([d[g[i]][0], p[i], i, g[i]])
gp = sorted(gp, key = lambda x: (-x[0], -x[1], x[2]))

answer = []
for gv, pv, i, gstr in gp:
    if d[gstr][1] > 1:
        continue
    answer.append(i)
    d[gstr][1] += 1

# answer = [x[2] for x in sorted(gp, key = lambda x: (-x[0], -x[1], x[2]))]
print(answer)
