def fac(num: int):
    if num > 1:
        return num*fac(num-1)
    else:
        return 1

print(fac(int(input())))