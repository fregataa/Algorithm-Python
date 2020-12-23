def solution(people, limit):
    answer = 0
    people = sorted(people)
    light, heavy = 0, len(people)-1

    while light < heavy:
        answer += 1
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
    
    if light == heavy:
        answer += 1

    return answer
        

# def solution(people, limit):
#     answer = 0
#     people = sorted(people)
    
#     while people:
#         answer += 1
#         aboard = people.pop()
#         if people and aboard > limit - people[0]:
#             continue
#         for i in range(len(people)-1, -1, -1):
#             if aboard + people[i] <= limit:
#                 people.pop(i)
#                 break
    
#     return answer

print(solution([70, 50, 80, 50], 100))
