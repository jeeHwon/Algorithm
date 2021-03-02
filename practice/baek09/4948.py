import math
N = 123456 * 2
array = [True for _ in range(N+1)]
for i in range(2, N+1):
    if array[i] == True:
        j = 2
        while i * j <= N:
            array[i*j] = False
            j += 1

while True:
    val = int(input())
    if val == 0:
        break
    cnt = 0
    for i in range(val+1, (val*2)+1):
        if array[i] == True:
            cnt += 1
    print(cnt)

# 실패 - 시간초과
# import math
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     array = [True for _ in range((2*n)+1)]
#     for i in range(2, int(math.sqrt(2*n)+1)):
#         if array[i] == True:
#             j = 2
#             while i * j <= (2*n):
#                 array[i*j] = False
#                 j += 1
#     cnt = 0
#     for i in range(n+1, (2*n)+1):
#         if array[i]:
#             cnt += 1
#     print(cnt)
