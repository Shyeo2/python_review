# ezen05-2
# boolean
# loop
'''
  참/거짓 자료형
    - 거짓(False) : 0, 리스트/튜플/사전, 
    - 참(True) : 이외에 실제 의미 있는 값들 

    - 7 => 참
      1 => 참
      0 => 거짓 
      " Hello Ezen" => 참
      "" => 거짓
      [1,2,3] => 참
      [] => 거짓
      () => 거짓 
'''
print(bool(7))
print(bool(1))
print(bool(0))
print(bool("Hello Ezen"))
print(bool([1,2,3]))
print(bool([]))
print(bool(()))

'''
  반복문
    for 원소 in 시퀀스데이터:

'''

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
  print(x)

print()

result = 0 
for i in range(1,51):   # 1부터 50까지 
  result += i           # 더하기 
print(result)


# 1부터 50까지의 수 중에서 10의 배수만 더하는 프로그램을 작성하시오.
num = 0
for i in range(1, 51):
  if i % 10 == 0:         # 10 으로 나누었을 때 나머지가 0 
    num += i
print(num)

print()

# enumerate()
naem_list = ['지수', '로제', '리사', '제니']
for i, element in enumerate(naem_list):
  print(i,element)

print()

# 구구단
for i in range(1, 10):
  for j in range(1, 10):
    print(i, "X " , j , " = ", i * j )

'''
  리스트 2개가 있습니다.
  리스트의 중앙값을 출력하는 코드를 작성하시오.
  단, 중앙값은 리스트가 홀수 개의 숫자에 대해서는 크기 순서대로 가장 가운데 있는 값이다
  리스트가 짝수 개의 숫자에 대해서는 가장 가운데 있는 두 개의 숫자의 평균이다.
  예) [5, 11, 2, 4] ==> 4.5
      [1, 3, 4, 5, 100] ==> 4 
'''

num1 = [10, 100, 25, 5, 11, 55]
num2 = [3, 2, 677, 99, 11, 6, 1001]

num1.sort()
print(num1)
num2.sort()
print(num2)

# 짝수인지 홀수인지 확인
len1 = len(num1)
len2 = len(num2)

if len1 % 2 == 0:    
  print((num1[int(len1/2)-1] + num1[int(len1/2)])/2) # 짝수 
else:
  print(num1[int(len1/2)])  #홀수

if len2 % 2 == 0:  
  print((num2[int(len2/2)-1] + num2[int(len2/2)])/2)   # 짝수 
else:
  print(num2[int(len2/2)])  #홀수
  
  
