input = input()
input = input.split(' ')
a = int(input[0])
b = int(input[1])
c = int(input[2])

print((a+b)%c)
print(((a%c) + (b%c)) % c)
print( (a*b)%c )
print( ((a%c) * (b%c)) % c )