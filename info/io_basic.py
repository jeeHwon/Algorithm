# 자주 사용되는 표준 입력방법
# input() : 한줄의 문자열을 입력받는 함수
# map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# list(map(int, input().split())) : 공백을 기준으로 구분된 데이터 입력시 사용
# a,b,c = map(int, input().split()) : 구분된 데이터 적을 때 사용

# 데이터 개수 입력
# n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
# data = list(map(int, input().split()))
# data.sort(reverse=True)
# print(data)

# 빠르게 입력받기
# import sys 
# data = sys.stdin.readline().rstrip()
# print(data)

# 자주 사용되는 표준 출력방법
# 기본 줄바꿈 방지
print('기본', end=" ")
print('줄바꿈', end=" ")
print('방지입니다')
answer = 5
print('정답은'+str(answer))

# f-string
answer = 7
print(f'정답은 {answer} 입니다')