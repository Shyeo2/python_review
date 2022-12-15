# ezen06-1
'''
  1) 숫자형 (int, float)
  2) 문자형 (str) : 큰 따옴표, 작은 따옴표 다 사용 가능 
  3) 리스트
      - 집합 구조
      - 데이터를 모아놓은 데이터 타입
      - 리스트 인덱싱 
          name = ['ezenit']

                'e' 'z' 'e' 'n' 'i' 't'
          index  0   1   2   3   4   5
 negative index -6  -5  -4  -3  -2  -1     

      - 리스트 값 변경
      - 리스트 자르기 
          name[0:2]
      - 리스트 요소 추가, 제거, 정렬, reverse 
      - 중첩 리스트  
'''

list_ = []
print(list_, type(list_))

student = ['Lisa', 'Jennie', 'Rose', 'Jisoo']
age = [20, 22, 21, 23]
print(student)
print(age)

print(student[1], age[1])
print(student[-1], age[-1])

student[1] = 'Sunhye'
age[1] = 23
print(student)
print(age)

print(student[1:2])
print(student[1:3])

student.reverse()
print(student)

student.append('mango')
print(student)

student.remove('mango')
print(student)

age.sort()
print(age)
age.sort(reverse=True)
print(age)

age.insert(0,2)
print(age)

age.pop(0)
print(age)

# 중첩 리스트 
stu_list = [student, age]
print(stu_list)

print(stu_list[0])
print(stu_list[])
