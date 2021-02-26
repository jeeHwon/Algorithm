# 투 포인터(Two Pointers)
# 리스트에 순차적으로 접근해야 할 떄 두개의 점 위치를 기록하면서 처리하는 알고리즘
# 시작점과 끝점 2개의 점으로 접근할 데이터의 범위 표현 가능
# 시간복잡도 => O(N)

# 문) 특정한 합을 가지는 부분 연속 수열 찾기
n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1,2,3,2,5] # 전체 수열 

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
print(count)