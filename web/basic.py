# 웹 요청
import requests
target = "http://google.com"
response = requests.get(url=target)
print(response.text) # <!doctype html><html itemscope="" ..

# REST(Representational State Transfer)
# 각 자원에 대하여 자원의 상태에 대한 정보를 주고받는 개발 방식

# REST의 구성요소
# 자원(Resource) : URI 이용
# 행위(Verb) : Http 메서드 이용
# 표현(Representations) : 페이로드를 이용

# REST API
# API(Application Programming Interface) : 프로그램이 상호작용하기 위한 인터페이스
# REST API : REST 아키텍쳐를 따르는 API
# REST API 호츨 : REST 방식을 따르고 있는 서버에 특정한 요청을 전송하는 것


# JSON(JavaScript Object Notation)
# 데이터를 주고받는데 사용하는 경량의 데이터 형식
# key와 value의 쌍으로 이루어진 데이터 객체를 저장
# 사용예제
import json

# 딕셔너리 데이터타입 데이터 선언
user = {
    "id" : "jenny",
    "password" : "1234!@#$",
    "age" : 30,
    "hobby" : ["football", "programming"]
}

# 파이썬 변수를 JSON 객체로 변환
json_data = json.dumps(user, indent=4)
print(json_data)

# JSON 데이터로 변환하여 파일로 저장
# with open("user.json", "w", encoding="utf-8") as file:
#    json_data = json.dump(user, file, indent=4)

# REST API 연습용 서비스
# 목킹(Mocking) : 어떠한 기능이 있는 것 처럼 흉내내어 구현한 것
# http://jsonplaceholder.typicode.com/

# REST API를 호출하여 회원정보를 처리하는 예제
import requests

# REST API 경로에 접속하여 응답(Response) 데이터 받아오기
target = "http://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

# 응답(Response) 데이터가 JSON 형식이므로 바로 파이썬 객체로 변환
data = response.json()

# 모든 사용자(user) 정보를 확인하며 이름 정보만 삽입
name_list = []
email_list = []
for user in data:
    name_list.append(user['name'])
print(name_list)
