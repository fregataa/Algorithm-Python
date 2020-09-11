b = "hit"
t = "cog"

words = ["hot", "dot", "dog", "lot", "log", "cog"]
answer = 0

chker = [True for _ in range(len(words))]
# def cmp(st1: str, st2: str):  
#     chk = False
#     for i in range(len(st1)):
#         if st1[i] != st2[i]:
#             if chk:
#                 return False
#             else:
#                 chk = True
#     return True

q = [b]
while q:
    l = []
    for node in q:
        for i in range(len(words)):
            if node == t:
                print(answer)
                exit()
                # return answer
            # if cmp(node, words[i]) and chker[i]:

            if sum([x!=y for x,y in zip(node, words[i])]) == 1 and chker[i]: # => AWESOME !!!
                l.append(words[i])
                chker[i] = False
    q = l[:]
    answer += 1

# return 0
print(0)