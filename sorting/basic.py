# 정렬(Sorting)
# 데이터를 특정한 기준에 따라 순서대로 나열하는 것


# 선택정렬 => O(N^2)
# 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것 반복
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프
print(array)


# 삽입 정렬 => O(N^2)
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
# 거의 정렬된 상태라면 빠르게 동작 -> O(N)
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소 반복
        if array[j] < array[j-1]: # 한칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j] # 스와프
        else:
            break
print(array)


# 퀵정렬 => O(N*logN) but 최악의 경우 O(N^2)
# 기준 데이터를 설정하고 그보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 일반적으로 가장 많이 사용
# 기본 1
# 첫번째 데이터를 기준 데이터(Pivot)로 설정
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array, start, end):
    if start >= end : # 원소가 1개인 겨웅 종료
        return
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while(left <= right): # 엇갈리기 전까지
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right) : # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else : # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[right], array[left] = array[left], array[right]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
quick_sort(array, 0, len(array)-1)
print(array)

# 파이썬의 장점을 살린 방식
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array 
    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))


# 계수 정렬
# 데이터의 개수가 N, 데이터 중 최댓값이 K 일 때 => O(N+K)
# 특정한 조건이 부합 될 때만 사용할 수 있지만 매우 빠르게 동작
# 데이터의 크기 범위가 제한되어 정수 형태로 표현 할 수 있을 때 사용 가능
# 동일한 값을 가지는 데이터가 여러개 등장 할 때 효과적으로 사용 가능

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)
for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

# 정렬 알고리즘 비교
# 정렬알고리즘 / 평균 시간 복잡도 / 공간 복잡도 / 특징
#   선택정렬   /     O(N^2)     / O(N)       / 아이디어가 간단
#   삽입정렬   /     O(N^2)     / O(N)       / 데이터가 거의 정렬 되어있을때 가장 빠름
#   퀵정렬     /     O(NlogN)   / O(N)       / 대부분의 경우 가장 적합, 충분히 빠름
#   계수정렬   /     O(N+K)     / O(N+K)     / 데이터의 크기가 한정되어 있는 경우 사용 가능 매우빠름
# 


# 두 배열의 원소 교체
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행
# 첫번째 인덱스부터 확인하며, 두배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break
print(sum(a))