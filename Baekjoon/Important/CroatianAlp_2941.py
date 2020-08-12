import re
print(len(re.sub('dz=|c=|c-|d-|lj|nj|s=|z=', '.', input())))


# calp = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
# line = input()
# count = len(line)
# for c in calp:
#     if c in line:
#         count -= line.count(c)
# print(count)


# calp = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
# line = input()
# for c in calp:
#     line = line.replace(c, '.')
# print(len(line))


# count = 0
# for c in calp:
#     while line.find(c) != -1:
#         line = line.replace(c, ' ', 1)
#         count += 1
# for c in line:
#     if c != ' ':
#         count += 1
# print(count)