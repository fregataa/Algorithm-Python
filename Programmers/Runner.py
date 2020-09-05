import collections as c

participant = ['leo', 'kim','park','kim']
completion = ['kim','leo', 'park']

answer = list(c.Counter(participant) - c.Counter(completion))
print(answer[0])

# answer = c.Counter(participant) - c.Counter(completion)
# print(list(answer.keys())[0])