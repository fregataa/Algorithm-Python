
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

i = len(triangle)-1
while i:
    for j in range(len(triangle[i])-1):
        if triangle[i][j] > triangle[i][j+1]:
            triangle[i-1][j] += triangle[i][j]
        else:
            triangle[i-1][j] += triangle[i][j+1]
    i -= 1

print(triangle[0][0])