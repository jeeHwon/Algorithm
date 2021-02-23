# 그리디
# 최적의 해 보장 가능한가? -> 정당성 분석

# 문) 거스름돈 주기 => 시간복잡도 화폐개수 K일 때 O(K)
n = 1260
count = 0
array = [500, 100, 50, 10]
for coin in array:
    count += n // coin
    n %= coin
print(count)
print("*" * 40)

# 문) 1이 될때 까지
# 어떤수 N이 1이 될때 까지 두가지 연산만 수행
#   1) N에서 1빼기, 2) N을 K로 나누기(나누어 떨어질때 only)
# 과정 수행 최소로 하는 프로그램
# => 가능한 나누기를 최대로 하자
# 내 답안
n, k = map(int, input().split())
cnt = 0
while n != 1:
    if n % k == 0:
        n = n // k
        cnt += 1
    else:
        n -= 1
        cnt += 1
print(cnt)
# log(N) 복잡도 가지는 답안
n, k = map(int, input().split())
cnt = 0
while True:
    target = (n // k) * k
    cnt += (n - target)
    n = target
    if n < k:
        break
    cnt += 1
    n //= k
cnt += (n - 1)
print(cnt)

# 문) 곱하기 혹은 더하기
data = input()
# 첫번째 문자를 숫자로 변경해 대입
result = int(data[0])
for i in range(1, len(data)):
    # 두 수 중 하나라도 0 또는 1이면 더하기, 나머지 곱하기
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)

# 문) 모험가 길드
# N명의 모험가, 공포도 X인 모험가는 반드시 X명 이상의 모험가 그룹
# 여행을 떠날수 있는 그룹수의 최댓값 입력: 5 /n 2 3 1 2 2 출력:2
n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0  # 총 그룹의 수
cnt = 0  # 현재 그룹에 포함된 모험가의 수
for i in data:  # 공포도 낮은 것 부터 차례로
    cnt += 1  # 현재 그룹에 해당 모험가 추가
    if cnt >= i:  # 현재 모험가 수가 현재 공포도 이상
        result += 1  # 총 그룹 수 증가
        cnt = 0  # 현재 그룹 모험가수 초기화
print(result)
