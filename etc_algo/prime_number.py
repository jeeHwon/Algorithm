# 소수(Prime Number)
# 1보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지 않은 자연수

# 소수 판별 함수(2이상의 자연수에 대하여)
# 기본 알고리즘 => 모든수를 하나씩 확인 => O(X)
def is_prime_number(x):
    # 2부터 (x-1)까지 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

# 약수의 성질
# 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭
# 즉, 모든 약수를 찾지 말고 제곱근까지 구하면 됨

# 소수의 판별: 개선된 알고리즘
# 2부터 X의 제곱근까지 연산 수행하므로 => O(N^1/2)
import math
def is_prime_number2(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

# 다수의 소수 판별
# 특정한 수 범위 안에 존재하는 모든 소수 찾기

# 에라토스테네스의 체 알고리즘
# 다수의 자연수에 대하여 소수 여부 판별시 사용하는 대표적 알고리즘
# 시간 복잡도 => O(NloglogN) 매우 빠름
# but 각 자연수에 대한 소수 여부 저장하므로 메모리가 많이 필요
import math

n = 100000000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
# 처음엔 모든 수가 소수(True) 인 것으로 초기화 (0과 1은 제외)
array = [True for i in range(n+1)]

# 에라토스테네스의 체 알고리즘 수행 
# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(n)+1)):
    if array[i] == True: # i가 소수인 경우 (남은 수의 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
