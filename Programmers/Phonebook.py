import re

# def find():
#     phone_book = ['1922', '197674223', '191']
#     for i in range(len(phone_book)):
#         p = re.compile(phone_book[i]+'[0-9]*')
#         for j in range(len(phone_book)):
#             if i==j:
#                 continue
#             a = p.match(phone_book[j])
#             if a:
#                 print(i, j, a.group())
#                 return False
#     return True
    
# print(find())


def find():
    phone_book = ['1922', '197674223', '191']
    phone_book.sort()
    
    for num1, num2 in zip(phone_book, phone_book[1:]):
        if num1.startswith(num2):
            return False
    return True

print(find())