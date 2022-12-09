#ezen04-2
#파이썬 데이터 타입(자료형)
#리스트, 튜플 

#리스트 자료형(순서O, 중복O, 수정O, 삭제O)

#선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Powerful', 'Health', 'Features']
e = [10, 100, ['Powerful', 'Health', 'Features']]

#인덱싱
print()
print('d : ', type(d), d)
print('d : ', d[1])
print('d : ', d[0] + d[1] + d[1])     #더하기 연산 
print('d :' , d[-1])
print('e : ', e[-1][1])             #e :  Health
#e = [10, 100, ['Powerful', 'Health', 'Features']] -1은  ['Powerful', 'Health', 'Features']전체 임
print('e : ', e[-1][1][4] )         #e :  t

#슬라이싱 
print()
print('d : ', d[0:3])
print('d : ', d[2:])
print('e : ', e[2][1:3])

#연산 
print()
print('c + d : ', c + d)       # 문자열 연결
print('c * 3 : ', c * 3)       # c * 3 :  [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4] n번 출력 

#수정
print()
c[0] = 4
print('c : ', c)
c[1:2] = ['a', 'b', 'c']      #   c :  [4, 'a', 'b', 'c', 3, 4]
print('c : ', c)
  #리스트 안에 리스트 형태 
c[1] =  ['a', 'b', 'c']       # 슬라이싱 말고 인덱싱 
print('c : ', c)              # c :  [4, ['a', 'b', 'c'], 'b', 'c', 3, 4]

#삭제 (remove, del, pop)
c[1:3] = []
print('c : ', c) 
del c[3]
print('c : ', c)  

#리스트 함수
a = [5, 2, 3, 1, 4]
print('a : ', a)

a.append(6)
print('a : ', a)

a.sort()
print('a : ', a)

a.reverse()
print('a : ', a)

print('a : ', a.index(5))  #a :  1

a.insert(2, 7)          # a.insert(n, a) n번째에 a 추가 
print('a : ', a)        # a :  [6, 5, 7, 4, 3, 2, 1]

a.remove(1)             # 
print('a : ', a)

print('a : ', a.pop())   # 제일 끝 remove 처리
print('a : ', a.pop())     
print('a : ', a)

print('a : ', a.count(4)) #갯수 

ex = [8, 9]
a.extend(ex)
print('a : ', a)

while a: 
  l = a.pop()
  print(6 is l)   #boolean 형  
'''
False
False
False
False
False
True
'''


#-----------------------------------------------------------------------
#튜플 (순서O, 중복O, 수정X, 삭제 X )
'''
  - 튜플(tuple) 자료형은 리스트와 유사
  - 리스트는 대괄호 []를 이용하지만, 튜플은 소괄호()을 사용함
  - 값이 변경되면 안되는 경우, 튜플을 사용하면 효과적임 
'''

#선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, 'Powerful', 'Health', 'Features')
e = (10, 100, ('Powerful', 'Health', 'Features'))

#인덱싱
print()
print('d : ', type(d), d)
print('d : ', d[1])
print('d : ', d[0] + d[1] + d[1])     #더하기 연산 
print('d :' , d[-1])
print('e : ', e[-1][1])             #e :  Health
#e = [10, 100, ['Powerful', 'Health', 'Features']] -1은  ['Powerful', 'Health', 'Features']전체 임
print('e : ', e[-1][1][4] )         #e :  t

#슬라이싱 
print()
print('d : ', d[0:3])
print('d : ', d[2:])
print('e : ', e[2][1:3])

#연산 
print()
print('c + d : ', c + d)       # 문자열 연결
print('c * 3 : ', c * 3) 

#튜플 함수
a = (5, 2, 3, 1, 4)

print('a : ', a)
print('a : ', a.index(5))
print('a : ', a.count(5))




