# 함수의 종류
# 내장함수 : 파이썬이 기본적으로 제공하는 함수
# 사용자 정의 함수 : 개발자가 직접 정의

# 함수 정의
# def 함수명(매개변수):
#   실행할 소스코드
#   return 반환값

# global : 함수 바깥에 선언된 변수를 바로 참조
a = 0
def func():
    global a
    a += 1
for _ in range(10):
    func() 
print(a)

# packing & unpacking
def operator(a,b):
    add_var = a + b
    sub_var = a - b
    return add_var, sub_var
a, b = operator(3,4)
print(a,b)

# 람다 표현식
# 내장함수에서 사용
array = [('jenny',29), ('rose',25), ('lisa',27)]
print(sorted(array, key=lambda x: x[1]))
# 여러개 리스트에 적용
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
result = map(lambda a, b: a + b, list1, list2)
print(list(result))
