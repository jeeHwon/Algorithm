# 이진탐색 => O(logN)
# "정렬되어 있는 리스트"에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# <=> 순차탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 탐색하는 방법

# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 타겟이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 타겟이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

# 이진 탐색 소스코드 구현 (반복문 구현)
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 타겟이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 타겟이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자하는값)을 입력받기
n, target = map(int, input().split())
# 전체 원소 입력 받기
array = list(map(int, input().split()))
# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)

# 파이썬 이진 탐색 라이브러리
# bisect_left(a,x): 정렬 순서 유지, 배열 a에 x 삽입할 가장 왼쪽 인덱스 반환
# bisect_right(a,x): 정렬 순서 유지, 배열 a에 x 삽입할 가장 오른쪽 인덱스 반환
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

# 값이 특정 범위에 속하는 데이터 개수 구하기
# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
# 배열 선언
a = [1,2,3,3,3,3,4,4,8,9]
# 값이 4인 데이터의 개수 출력
print(count_by_range(a, 4, 4))
# 값이 -1~3 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
