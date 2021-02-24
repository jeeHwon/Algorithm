# BFS(Breadth-First Search)
# 너비 우선탐색
# 큐 자료구조 이용
# 그래프에서 가까운 노드부터 우선적으로 탐색
# 1) 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 2) 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중에서 방문하지 않은 
#   노드를 모두 큐에 삽입, 방문 처리
# 3) 더 이상 2번의 과정을 수행할 수 없을 때 까지 반복

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들은 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9
# 정의된 BFS 함수 호출
bfs(graph, 1, visited)


# 미로 탈출
# 첫째 줄에 두 정수 N, M
# 최초위치 (1,1) 미로 출구 (N,M) 한번에 한칸 이동 
# 괴물있는 부분 0, 없는 부분 1, 탈출하기 위해 움직이는 최소 칸수

#BFS 소스코드 구현
def bfs(x, y):
    # 큐(queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로찾기 공간 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # 가장 우측 하단까지의 최단거리 반환
    return graph[n-1][m-1]

from collections import deque
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# 이동할 네 가지 방향 정의(상하좌우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# BFS를 수행한 결과 출력
print(bfs(0,0))
