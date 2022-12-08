#ezen02-2
#파이썬 기초 코딩

import sys

# Python 3.x 입력 인코딩 
print(sys.stdin.encoding)

# Python 3.x 출력 인코딩 
print(sys.stdout.encoding)

my_name = "SunHye"
# 조건문
if my_name == "SunHye":
  print("ok!!")

이름 = "선혜"
print(이름)

def 인사():
  print("아듀 2022년, 해피뉴이어입니다.")

인사()

#클래스 
class Cookie:
  pass

#객체 생성
cookie = Cookie()

#객체 정보값 출력
print(id(cookie))

#외부 설치 패키지 테스트 
import simplejson as json

test_dict = {'1' : 95, '4' : 77, '3' : 65, '5' : 100, '2' : 88}

#오름차순으로 정렬 sort_keys=True
print(json.dumps(test_dict, sort_keys=True))

#들여쓰기
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))

