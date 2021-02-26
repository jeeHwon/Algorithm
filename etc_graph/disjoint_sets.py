# 기타 그래프 이론

# 서로소 집합(Disjoint Sets)
# 공통원소가 없는 두 집합
# 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# 연산1) 합집합(Union) : 두개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
# 연산2) 찾기(Find) : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
# 서로소 집합 자료구조 => 합치기 찾기(Union Find) 자료구조라고도 한다


# 서로소 집합 자료구조 기본 구현 : 최악의 경우 => O(V))
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수(V)와 간선의 개수(E, 연산의 개수) 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화 하기

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속합 집합 출력하기
print('각 원소가 속한 집합 :', end="")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")
print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end="")
for i in range(1, v+1):
    print(parent[i], end=" ")
# ================================================================

# 서로소 집합 자료구조 경로압축
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x): # ===========이곳만 수정
    # 루트 노드를 찾을 때까지 재귀호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수(V)와 간선의 개수(E, 연산의 개수) 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화 하기

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속합 집합 출력하기
print('각 원소가 속한 집합 :', end="")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")
print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end="")
for i in range(1, v+1):
    print(parent[i], end=" ")
#==================================================================

# 서로소 집합을 활용한 사이클 판별
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x): # ===========이곳만 수정
    # 루트 노드를 찾을 때까지 재귀호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수(V)와 간선의 개수(E, 연산의 개수) 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화 하기

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다")
else:
    print("사이클이 발생하지 않았습니다")
#==================================================================

# 신장 트리
# 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미

# 최소 신장 트리
# 최소한의 비용으로 구성되는 신장 트리를 찾을 때

# 크루스칼 알고리즘 
# 간선의 개수 E개 일때 시간복잡도 => O(ElogE)
# 대표적인 최소 신장 트리 알고리즘
# 그리디 알고리즘으로 분류
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x): 
    # 루트 노드를 찾을 때까지 재귀호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수(V)와 간선의 개수(E, 연산의 개수) 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화 하기

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫번쨰 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)