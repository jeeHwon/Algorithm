# 최단 경로 문제(Shortest Path)
# 가장 짧은 경로를 찾는 알고리즘
# 각 지점은 노드로 표현, 지점간 연결된 도로는 간선으로 표현

# 우선순위 큐(Priority Queue)
# 노드의 개수가 10,000개 넘는 경우 => 시간초과 문제 
# 우선순위가 가장 높은 데이터를 먼저 삭제하는 자료구조

# 힙(Heap)
# 우선순위 큐를 구현하기 위해 사용하는 자료 구조
# 최소힙과 최대힙이 있음
# 우선순위큐 구현 by 리스트 => 삽입시간(O(1)), 삭제시간(O(N))
# 우선순위큐 구현 by 힙 => 삽입시간(O(logN)), 삭제시간(O(logN))

# 힙라이브러리 사용예제 - 최소힙
import heapq
# 오름차순 힙정렬(Heap Sort)
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
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 힙라이브러리 사용예제 - 최대힙
import heapq
# 내림차순 힙정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)






