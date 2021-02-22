# ==========================실수형==========================
# 실수형 오차 발생 문제
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)
print('*'*30)

# round 함수 활용
a = 0.3 + 0.6
print(round(a,4))

if round(a,4) == 0.9:
    print(True)
else:
    print(False)
print('*'*30)

# 나누기 연산자 / : 실수형
# 나머지 연산자 %
# 몫 연산자 //

a = 7
b = 3
print('나누기',a/b)
print('몫',a//b)
print('나머지',a%b)
print('*'*30)

# ==========================리스트==========================
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 리스트 컴프리헨션
# 0부터 9까지의 수를 포함하는 리스트 
array = [i for i in range(10)]
print(array)

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i*i for i in range(1,10)]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0]* m for _ in range(n)]
print(array)
print('*'*30)

# 리스트 관련 메서드
list = [1,2,3]
list.append(4) # 원소 삽입
list.sort() # 오름차순 정렬
list.sort(reverse=True) # 내림차순 정렬
list.reverse() # 순서 뒤집기
list.insert(1,'a') # 인덱스에 삽입
list.count('a') # 특정 값 갯수 카운트
list.remove('a') # 하나만 제거

# 리스트에서 특정값을 가지는 원소 모두 제거
a = [1,2,3,4,5,5,5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)
print('*'*30)


# ==========================튜플==========================
# 리스트 =[] 튜플 =()
# 서로 다른 성질의 데이터 묶어서 관리 할대
# 데이터의 나열을 해싱의 키값으로 사용 할 때
# 리스트 보다 메모리를 효율적으로 사용해야 할 때

# ==========================딕셔너리==========================
# 딕셔너리 = {key:value, }
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
print(data)
if '사과' in data:
    print("'사과'를 key로 가지는 데이터 존재")
key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)
for key in key_list:
    print(key, ':', data[key])
print('*'*30)

# ==========================집합==========================
# set = {} 중복X 순서X
a = set([1,1,1,1,2,3,4,4,5])
print(a)
b = {3,4,5,6,7}
print('합집합:',a|b)
print('교집합:',a&b)
print('차집합:',a-b)
b.add(8) # 새로운 원소 추가
b.update([9,10]) # 새로운 원소 여러개 추가
b.remove(10) # 특정 원소 삭제