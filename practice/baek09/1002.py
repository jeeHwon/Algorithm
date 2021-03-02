import math
t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if x1==x2 and y1==y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    if r1 > r+r2 or r2 > r+r1 or r > r1+r2:
        print(0)
    elif r1 == r+r2 or r2 ==r+r1 or r1+r2==r:
        print(1)
    else:
        print(2)

