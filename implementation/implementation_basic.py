# 구현
# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 경우
# 1) 알고리즘은 간단, 코드가 지나치게 길때
# 2) 실수 연산 다루고, 특정 소수점 자리까지 출력해야하는 문제
# 3) 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
# 4) 적절한 라이브러리를 찾아서 사용해야 하는 문제

# 방향벡터
# 동,북,서,남
dx = [0,-1,0,1]
dy = [1,0,-1,0]
# 현재위치
x, y = 2, 2
for i in range(4):
    # 다음위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)


# 문) 상하좌우 문제
# (1,1)부터 R L U D
# R L U D
dx = [0,0,-1,1]
dy = [1,-1,0,0]
n = int(input())
s = input().replace(" ","").replace("R","0").replace("L","1").replace("U","2").replace("D","3")
x ,y= 1, 1
for i in s:
    if (0 < x + dx[int(i)] <= n) and (0< y + dy[int(i)] <= n):
        x += dx[int(i)]
        y += dy[int(i)]
    else:
        continue
print(x, y)
# 모답
n = int(input())
x, y = 1, 1
plans = input().split()
# R L U D
dx = [0,0,-1,1]
dy = [1,-1,0,0]
move_types = ['R','L','U','D']
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx> n or ny > n: # 공간 벗어나는 경우 무시
        continue
    x, y = nx , ny
print(x, y)


# 완전탐색문제(Brute Forcing)
# 문) 시각 => 하루 86400초 => 1초에 2천만번 수행 범위 내
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지
# 모든 시각 중 3이 하나라도 포함된 모든 경우의 수 구하기
n = int(input())
secs = 3600 * (n + 1)
h, m, s = 0, 0, 0
result = 0
for i in range(secs):
    if (str(h).find('3') != -1) or (str(m).find('3') != -1) or (str(s).find('3') != -1):
        result += 1
    if s == 59 and m == 59:
        h += 1
        m = 0
        s = 0
    elif s == 59:
        m += 1
        s = 0
    s += 1
print(result)    
# 모답
h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)


# 문) 왕실의 나이트
#   a b c d e f.. (8칸 x 8칸)
# 1
# 2
# 3
# 나이트가 움직일수 있는 모든 경우의 수
# 입력예시 a1 => 출력예시 2
s = input()
x_type = ['a','b','c','d','e','f','g','h']
dx = [-1,1,-2,-2,1,-1,2,2]
dy = [-2,-2,-1,1,2,2,-1,1] 
x = int(s[1])
y = x_type.index(s[0]) + 1
cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 < nx < 9 and 0 < ny < 9:
        cnt += 1 
print(cnt)
# 모답
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)


# 문) 문자열 재정렬
# 알파벳 대문자와 숫자로 입력 받아 알파벳 오름차순 + 숫자는 더한값 이어서 출력
input_data = input() # 0 9 A a => 48 57 65 97
ss = sorted(input_data)
f = ''
b = 0
for s in ss:
    if ord(s) < 65 :
        b += int(s)
    else:
        f += s
print(f+str(b)) # -> 숫자가 없는 경우 오답
# 모답
data = input()
result = []
value = 0
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()
if value != 0:
    result.append(str(value))
print(''.join(result))
