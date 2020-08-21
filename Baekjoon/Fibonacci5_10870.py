# def fibo(count: int):
#     if count > 2:
#         return fibo(count-1) + fibo(count-2)
#     elif count == 2 or count == 1:
#         return 1
#     else:
#         return 0

def fibo(count: int):
    if count < 2:
        return count
    return fibo(count-1) + fibo(count-2)

print(fibo(int(input())))