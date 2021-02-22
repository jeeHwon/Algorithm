# 실수형
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

# 리스트
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
