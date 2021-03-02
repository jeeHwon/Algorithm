import math
while True:
    n = int(input())
    if n == 0:
        break
    array = [True for i in range((2*n)+1)]
    for i in range(2, int(math.sqrt(2*n)+1)):
        if array[i] == True:
            j = 2
            while i * j <= (2*n):
                array[i*j] = False
                j += 1
    cnt = 0
    for i in range(n+1, (2*n)+1):
        if array[i]:
            cnt += 1
    print(cnt)
