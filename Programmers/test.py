# from collections import deque
# def solution1(k):
#     if k<2:
#         return 0
#     answer =0 
#     able_dict = {2:1, 3:1, 4:1, 5:3, 6:3, 7:1}
#     dp_k = []
#     dp_n = []
#     q = deque([[k,1]])
#     i=1
#     while q:
#         # print(q)
#         top = q.popleft()
#         remain = top[0]
#         num = top[1]
#         if remain==0:
#             answer += num
#             continue
#         for a in able_dict.keys():
#             if remain < able_dict[a]:
#                 continue
#             if a==6 and i and remain>6:
#                 q.append([remain-a, num*2])
#                 continue
#             q.append([remain-a, num*able_dict[a]])
#         i = 0
#     return answer

def solution(k):
    answer =0 
    able_dict = {2:1, 3:1, 4:1, 5:3, 6:2, 7:1}
    if k<8:
        able_dict[6] = 3
    q=[[0,1]]       #   [[지금까지 쓴 막대기 수, 경우의 수]]
    while q:
        dict_q = {} #   dp용 딕셔너리
        for num_of_bar, num_of_way in q:
            if num_of_bar == k:
                answer += num_of_way
                continue
            elif num_of_bar > k:
                continue
            for a in able_dict.keys():
                if num_of_bar + a in dict_q:
                    dict_q[num_of_bar+a] += num_of_way*able_dict[a]
                else:
                    dict_q[num_of_bar+a] = num_of_way*able_dict[a]
        q = list(map(lambda x: [x, dict_q[x]], dict_q.keys()))
        able_dict[6] = 3
        # print(q)

    return answer

print(solution(50))