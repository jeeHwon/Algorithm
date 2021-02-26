# 플로이드 워셜(Floyd-Warshall) 알고리즘 => O(N^3)
# 간선이 적을 때, 노드가 500개 이하일때 사용 고려
# 단계별로 거쳐가는 노드를 기준으로 알고리즘 수행
# 다만, 매 단계마다 방문하지 않은 노드중에 최단거리를 찾는 과정 필요 X
# 2차원 테이블에 최단거리 정보 저장, 다이나믹 프로그래밍 유형에 속함
# 각 단계마다 특정한 노드 k를 거쳐 가는 경우를 확인
# 점화식 : Dab = min(Dab, Dak + Dkb)

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 INFINITY 출력
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()



# 미래도시 문제
# 1~N 회사 K 거쳐서, 간선 시간 모두 1 양방향 가능
INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b= map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 거쳐갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

result = graph[1][k] + graph[k][x]

if  result >= INF:
    print("-1")
else:
    print(result)


