# 우선순위 큐(Priority Queue)
# 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
# 우선순위에 따라 처리하고 싶을 때 사용
# 예시) 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야 하는 경우
# 데이터 개수가 N개 일때 삽입, 삭제시간 => O(NlogN)

# 힙(Heap)
# 완전 이진 트리 자료구조 => 루트-왼쪽자식-오른쪽자식 순서로 차례대로 삽입되는 트리
# 항상 루트노드를 제거
# 최소힙(min heap) : 루트 노드가 최소값 => 값이 작은 데이터 우선제거
# 최대힙(max heap) : 루트 노드가 최대값 => 값이 큰 데이터 우선제거

# 최소힙 구성함수 : Min-Heapify()
# 상향식 - 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우 위치 교체
# 새로운 원소가 삽입, 제거될 때 O(logN)의 시간복잡도로 힙성질 유지

# 우선순위 큐 라이브러리 활용한 힙 정렬 구현예제
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])
