'''
1. 아래 문자열의 길이를 구하시오.
    q1 = "fjdldionelamdmsd'1322qdmfgvfvc'xv-=dfdfdsf"
2. 화면에 기호 * 100개를 표시하시오.
3. 문자열 "30"을 각각 정수형, 실수형, 복소수형, 문자형으로 변환하시오.
4. 다음 문자열 "Niceyear"에서 "year" 문자열만 추출하시오.
    str = "Niceyear"
5. 다음 문자열을 거꾸로 출력하시오.
    str = "Strawberry"
6. 다음 문자열에서 '-'을 제거 후 출력하시오.
    phoneNumber = "010-5555-9999"
7. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하시오.
  url = "http://ezenac.co.kr"
8. 다음 문자열을 모두 대문자, 소문자로 각각 출력해 보시오.
  str = "NiceYear"
9. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하시오.
  str = "abcdefghijklmn"
10. 다음 리스트에서 "Apple" 항목만 삭제하시오.
  list = ["Banana" , "Apple", "Orange"]

'''

# 1. 아래 문자열의 길이를 구하시오. q1 = "fjdldionelamdmsd'1322qdmfgvfvc'xv-=dfdfdsf"
q1 = "fjdldionelamdmsd'1322qdmfgvfvc'xv-=dfdfdsf"
print('1. q1의 길이 : ', len(q1))

# 2. 화면에 기호 * 100개를 표시하시오.
print('2. * 100개 :' ,'*' * 100)

# 3. 문자열 "30"을 각각 정수형, 실수형, 복소수형, 문자형으로 변환하시오.
print('3. 정수형 : \t', int("30"))
print('3. 정수형 : \t', float("30"))
print('3. 정수형 : \t', complex("30"))
print('3. 정수형 : \t', str(30))

# 4. 다음 문자열 "Niceyear"에서 "year" 문자열만 추출하시오.
str = "Niceyear"
print('4. 문자추출',str[4:])

# 5. 다음 문자열을 거꾸로 출력하시오.      # ::전체 출력 
str = "Strawberry"                
print('5. reverse :' , str[::-1])

# 6. 다음 문자열에서 '-'을 제거 후 출력하시오.
# 정규 표현식 
import re
phoneNumber = "010-5555-9999"
print('6. -을 제거 : ' , re.sub('[^0-9]', '', phoneNumber) )

# 7. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하시오.
url = "http://ezenac.co.kr"
print('7. http:// 제거 ', url[7:])
url_idx = url.index('''http://''')
print('7. http:// 제거 ', url[url_idx+7: ])

# 8. 다음 문자열을 모두 대문자, 소문자로 각각 출력해 보시오.
str = "NiceYear"
print('8. 대문자 : ', str.upper())
print('8. 소문자 : ', str.lower())

# 9. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하시오.
str = "abcdefghijklmn"
print('9. 슬라이싱 : ', str[2:5] )

# 10. 다음 리스트에서 "Apple" 항목만 삭제하시오.
list = ["Banana" , "Apple", "Orange"]
list.remove("Apple")
print('10. Apple 삭제 :' , list)