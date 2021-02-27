# 실전에서 유용한 표준 라이브러리
# itertools : 순열, 조합
# heapq : 힙자료구조, 우선순위 큐
# bisect : 이진탐색
# collections : 덱, 카운터
# math : 팩토리얼, 제곱근, 최대공약수, 파이

# 내장함수
# sum(), min(), max()
print(sum([3,4,5]))
print(min(3,4,5))
print(max(3,4,5))
# eval
print(eval("3*(1+4)")

# sorted()
result = sorted([9,1,6,3,4])
reverse_result = sorted([9,1,6,3,4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key : 정렬 순서 지정 가능 주로 lambda 형태
array = [('jenny',3), ('rose',5), ('lisa',4)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

# 순열과 조합
# 순열 : 서로 다른 n개에서 서로 다른 r개 선택해 줄세우기 nPr
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data,3))
print('순열',result)

# 조합 : 서로 다른 n개에서 서로 다른 r개 순서 상관없이 선택 nCr
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data,3))
print('조합',result)

# 중복 순열
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data,repeat=2))
print('중복순열',result)

# 중복 조합
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data,2))
print('중복조합',result)

# Counter : 등장횟수 세기
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue'])
print(dict(counter))

# 최대공약수(GCD)와 최소공배수(LCM)
import math
def lcm(a, b):
    return a * b // math.gcd(a,b)
a = 21
b = 14
print(math.gcd(a,b))
print(lcm(a,b))