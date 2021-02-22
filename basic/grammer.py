# 조건문
# 기본형태
# if 조건문1 : 
#   코드
# elif 조건문2 :
#   코드
# else:
#   코드

# 논리연산자
# X and Y : 모두 참일때 참
# X or Y : 하나만 참이어도 참
# not X : 거짓일때 참

# 기타연산자
# x in 리스트 : 리스트에 x 있을 때 참
# x not in 문자열 : 문자열에 x 있을 때 참

# pass
# 비워놓고 싶을 때 -> 아무것도 처리안하고 넘어감

# 조건문 간소화 (조건문 실행코드가 한줄일 경우)
score = 85
if score > 80: result = "success"
else: result = "fail"
print(result)

# 조건문 표현식(if~ else 한줄 작성시)
result = "성공" if score > 80 else "실패"
print(result)

# 조건문내 부등식
# if x > 0 and x < 20 을
# if 0 < x < 20 으로 표현가능

# 반복문
# for문
# for 변수 in 리스트(or 튜플등) : 첫번째 인덱스부터 차례로 방문
# for 변수 in range(끝값+1) : 0부터 값 차례로 순회할 때
# for 변수 in range(시작값, 끝값+1) : 연속적인 값 차례로 순회할 때
# cotinue : 반복문에서 남은 코드 실행을 건너뛰고 다음 반복 진행
# break : 반복문 즉시 탈출