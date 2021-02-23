# 그래프 탐색 알고리즘
# 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

# 스택(stack)
# stack = []
# stack.append() : 삽입
# stack.pop() : 삭제
# print(stack[::-1]) # 최상단 원소부터 출력
# print(stack) # 최하단 원소부터 출력

# 큐(queue)
# 시간복잡도 위해 deque 라이브러리 사용
# from collections import deque
# queue = deque()
# queue.append() : 삽입
# queue.popleft(): 삭제
# print(queue) : 먼저 들어온 순서대로 출력
# print(queue.reverse()) : 나중에 들어온 원소부터 출력

# 재귀함수(Recursive Function)
# 자기 자신을 다시 호출하는 함수
# 종료 조건을 명시해 무한히 호출되는 것 방지
# 반복문과 호환가능 유불리 따져서 사용할것

# 팩토리얼 구현 예제
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)
print('반복적:',factorial_iterative(5))
print('재귀적:',factorial_recursive(5))

# 최대공약수(GCD) 계산 => 유클리드 호제법
# 두 자연수 A, B에 대해 A를 B로 나눈 나머지 R
# A와 B의 최대공약수는 B와 R의 최대공약수와 같다
def gcd (a, b):
    if a % b == 0:
        return b
    r = a % b
    return gcd(b, r)
print(gcd(192, 162))
