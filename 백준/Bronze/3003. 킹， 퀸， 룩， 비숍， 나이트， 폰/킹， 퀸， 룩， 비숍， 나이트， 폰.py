piece = [1,1,2,2,2,8]
n = list(map(int, input().split()))

for i in range(len(piece)):
    print(piece[i] - n[i], end=' ')