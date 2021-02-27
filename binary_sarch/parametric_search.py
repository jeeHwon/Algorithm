# 파라메트릭 서치(Parametric Search)
# 최적화 문제를 결정문제(yes or no) 로 바꾸어 해결하는 기법
# 예시 - 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
# 일반적으로 이진탐색을 이용하여 해결 가능

# 문) 떡볶이 떡 만들기 
# 떡의 개수 N, 요청한 떡의 길이 M 절단기로 자른 나머지를 준다
# 절단기에 설정할 수 있는 높이의 최댓값 출력
# 현재 이 높이로 자르면 조건 만족가능한가? => 탐색범위를 좁혀가며
# 절단기 높이는 10억까지의 정수중 하나, 큰 탐색범위 => 가장 먼저 이진탐색

# 떡의 개수(N)와 요청한 떡의 길이 (M)을 입력
n, m = map(int, input().split())
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))
# 이진탐색을 위한 시작점과 끝점을 설정
start = 0
end = max(array)
# 이진 탐색 수행 (반복적)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때 떡의 총길이 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽탐색)
    else:
        result = mid
        start = mid + 1
print(result)