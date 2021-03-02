N = 10000 
array = [True for _ in range(N+1)]
for i in range(2, N+1):
    if array[i] == True:
        j = 2
        while i * j <= N:
            array[i*j] = False
            j += 1

def get_part(n):
    for i in range(n//2, 1, -1):
        if array[i] == False:
            continue
        else:
            j = n - i
            if array[j] == True:
                return min(j,i), max(j,i)

T = int(input())

for i in range(T):
    n = int(input())
    a, b = get_part(n)
    print(a, b)