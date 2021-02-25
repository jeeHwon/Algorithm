# 다이나믹 프로그래밍
# = 동적 계획법
# 메모리를 적절히 사용하여 수행시간 효율성을 비약적으로 향상 시키는 방법
# 이미 계산된 결과는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 
# 구현 -> 일반적으로 탑다운 % 바텀업
# 조건1) 최적 부분구조(Optimal Substructure) : 큰 문제를 작은 문제로 나누고, 작은문제의 답을 모아 해결
# 조건2) 중복되는 부분문제(Overlapping Subproblem) 동일한 작은 문제를 반복적으로 해결

# 피보나치 수열(Fibonacci Function)
# 점화식 : 인접한 항들 사이의 관계식
# an = an-1 + an-2   /   a1 = 1, a2 = 1 => 피보나치 수열의 점화식

# 피보나치함수 (단순 재귀함수 구현) => 지수시간 복잡도O(2^N) by 중복되는 부분문제
def fibo(x):
    if x == 1 or x ==2:
        return 1
    return fibo(x-1) + fibo(x-2)
print(fibo(7))


# 메모이제이션(Memoization) => 시간복잡도 O(N)
# 한번 계산한 결과를 메모리 공간에 미모하는 기법
# 값을 기록해 놓는 점에서 캐싱(Cashing)이라고도 한다

# 탑다운: 하향식(재귀함수 이용)
# 피보나치 수열: 탑다운 다이나믹 프로그래밍 소스코드
# 한번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100
# 피보나치 함수를 재귀함수로 구현
def fibo_topdown(x):
    # 종료조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 결과 반환
    d[x] = fibo_topdown(x-1) + fibo_topdown(x-2)
    return d[x]
print(fibo_topdown(50))

# 바텀업: 상향식(반복문 이용)
# 전형적인 다이나믹 프로그래밍 형태, 결과저장용 리스트 : DP테이블
# 피보나치 수열: 바텀업 다이나믹 프로그래밍 소스코드
# 앞서 계산된 결과를 저장하기 위한 DB 테이블 초기화
d = [0] * 100
# 첫번째 피보나치 수와 두번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99
# 피보나치 함수를 반복문으로 구현
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])


# 문) 개미전사 - 바텀업 다이나믹 프로그래밍 
# ai = i번째 식량창고까지의 최적의 해(얻을 수 있는 식량 최대값)
# ki = i번째 식량창고에 있는 식량의 양
# 점화식 : ai = max(ai-1,  ai-2 + ki)
n = int(input())
array = list(map(int, input().split()))
# 앞서 계산된 결과를 저장하기 위한 DB 테이블 초기화
d = [0] * 100
# 다이나믹 프로그래밍 - 바텀업
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])
print(d[n-1])


# 문) 1로 만들기
# 5로 나누어 떨어지면 나누고, 3, 2 도 마찬가지
# 1로 뺴기 가능. 1로 만드는 최소 연산수
x = int(input())
d = [0] * (x+1)
# 다이나믹 프로그래밍 - 바텀업
for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    # 현재의 수가 3로 나누어 떨어지는 경우
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)
print(d[x])