
def out_star(n):
    global graph

    if n == 3:
        graph[0][:3] = [1]*3
        graph[1][:3] = [1,0,1]
        graph[2][:3] = [1]*3
        return 
    
    tmp = n//3
    out_star(n//3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(tmp):
                graph[tmp*i+k][tmp*j:tmp*(j+1)] = graph[k][:tmp]


N = int(input())

graph = [[0 for i in range(N)] for i in range(N)]

out_star(N)

for i in graph:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()