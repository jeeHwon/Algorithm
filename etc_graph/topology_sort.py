# 위상정렬(Topology Sort)
# 사이클이 없는 방향 그래프(DAG)의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열 의미
# 집입차수(Indegree) : 특정한 노드로 들어오는 간선의 개수
# 진출차수(Outdegree) : 특정한 노드에서 나가는 간선의 개수
# 큐를 이용하여 구현 가능 (스택도 가능)
# 예시) 선수과목을 고려한 학습 순서 설정
# 여러가지 답 존재 가능, 모든 원소 방문 전 큐가 빈다면 사이크 존재한다고 판단가능
# 위상 정렬 위해 차례로 모든 노드를 확인하고, 각 노드에서 나가는 간선을 차례로 제거
# 따라서 시간 복잡도 => O(V+E)

from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 방향그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 A에서 정점 B로 이동가능
    # 진입차수를 1증가
    indegree += 1

# 위상정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=" ")
topology_sort()

