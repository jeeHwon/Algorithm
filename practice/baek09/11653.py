import math
n = int(input())
array = []
def get_num(num):
    global n
    mid = int(math.sqrt(num))
    for i in range(mid, 1, -1):
        if num % i == 0:
            n = num // i
            return get_num(n), get_num(i)
    array.append(num)

get_num(n)
array.sort()
for i in array:
    if i == 1:
        break
    print(i)

