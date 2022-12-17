# ezen06-5
'''
  6) Dataframe 
    - index 행
    - columns 열 
    - 데이터 선택 (slicing)
      - 데이터 위치를 활용한 데이터 가공 : loc(), iloc()
    - 데이터 삭제 (drop)
      - 필요없는 데이터 삭제
      - 행(index), 열(columns)단위로 삭제 
    - 중복 데이터 삭제 (duplicated(), drop_duplicates())
'''

import pandas as pd 

df = pd.DataFrame()
print(type(df))

stu_list = [['Lisa', 'Jisoo', 'Rose', 'Jennie'], [19, 15, 16, 17]]
print(stu_list)

#중첩된 리스트를 DataFrame으로 변경 
df = pd.DataFrame(stu_list)
print(df)

print()

#행열 바꾸기
df = df.T
print(df)

print()

#컬럼 이름 
colums_name = ['name', 'age']
df.columns = colums_name
print(df)


'''
  "I am quitting this exam"
  "This is the quickest approach I ever seen"
  "The king should make quick decision "

  문장을 입력하다가 'q'라고 작성을 하였습니다.
  원래는 'w'를 작성해야했습니다.

  주어진 문장들을 모두 맞게 변경하시오. replace()

  "I am wuitting this exam"
  "This is the wuickest approach I ever seen"
  "The king should make wuick decision "

'''

ex_list = ['I am quitting this exam', 'This is the quickest approach I ever seen', 'The king should make quick decision']
result_list = []
print(ex_list)

for x in ex_list:
  x = x.replace('q', 'w')
  result_list.append(x)
print(result_list)


test_list = ['I am quitting this exam', 'This is the quickest approach I ever seen', 'The king should make quick decision']
for sentence in test_list:
  print(sentence.replace("q","w"))


# 주어진 문장들에 대해서 몇 개의 단어가 있는지 출력하시오. (split())
# 5
# 8
# 6
for sentence in test_list:
  print(len(sentence.split()))

'''
  차범근 축구감독이 미래 축구 꿈나무를 선별하여 축구부를 만듭니다.
  키가 175cm이상인 사람들을 뽑아서 축구부를 결성합니다. 
  soccer_team이라는 빈 리스트를 작성하여, 축구부가 될 사람들의 이름만 축가하는 코드를 작성해 보시오.
'''
candidates = {"박지성" : 146, "이강인" : 160, "김승규" : 167, "이승우 " : 175.3,  "김민재" : 207}
soccer_team = []

# 방법1
for name, height in candidates.items():
  if height >= 175:
    soccer_team.append(name)

print(soccer_team)

# 방법2
for i in candidates:
  if candidates[i] >= 175:
    soccer_team.append(i)

print(soccer_team)

print()

# 방법3
soccer_team2 = [name for name, height in candidates.items() if height >= 175]
print(soccer_team2)
  
print()
# 구구단 출력(for문)
# '{인덱스0}, {인덱스1}'.format(값0, 값1)
for num2 in range(1, 10):
  for num1 in range(2, 10):
    print("{} X {} = {}".format(num1, num2, num1*num2), end="\t")
  print()
  
print()
# 구구단 가로 출력 (while문)

# num2 = 1
# num1 = 2
# while num2 < 10:
#   while num1 < 10:
#     print("{} X {} = {}".format(num1, num2, num1*num2), end="\t")
#     num1 += 1
#   print()
#   num2 += 1

# num2 = 1
# while num2 < 10:
#   num1 = 2
#   while num1 < 10:
#     print("{} X {} = {}".format(num1, num2, num1*num2), end="\t")
#     num1 += 1
#   print()
#   num2 += 1

print()
'''
  얼마나 시간이 걸리고 갯수가 몇개인지 확인하시오.
  - for문을 이용하여 1부터 1000000까지의 숫자중에서 3의 배수인 숫자들을 찾고, 몇개가 있는지 알아보자.
  - 이 코드를 수행하는데 걸린 시간을 확인해보자. 

'''
import time
start = time.time()

ls = []
for x in range(1,1000001):
  if x % 3 == 0:
    ls.append(x)

end = time.time()
print(f"소요시간 : {end - start}")
print(f"리스트 원소 개수 : {len(ls)}개")

# 앞서 구구단은 얼마나 시간이 걸릴까요?

start1 = time.time()
for num2 in range(1, 10):
  for num1 in range(2, 10):
    print("{} X {} = {}".format(num1, num2, num1*num2), end="\t")
  print()
  
print()
end1 =  time.time()
print(f"소요시간 : {end1 - start1}")

'''
  도준이가 5000원 이상 소지하고 있을 경우 택시를 타고 집에 귀가할 수 있지만, 
  걸어서 귀가할 수도 있습니다.
  택시를 탈 경우 , 3000원이 소비됩니다. 잔액을 표시하시오.

  2000원 이상 있을 경우 버스틑 타고 귀가할 수 있습니다.
  버스를 탈 경우 , 1000원이 소비됩니다. 잔액을 표시하시오.

  2000원 미만일 경우 걸어서 귀가할 수 있습니다.
  위 조건을 반영하는 코드를 작성하시오.
'''

money = 2500
taxi = True

if money >= 5000:
  if taxi:
    print("택시타고 고고씽")
    print(f"얼마남았을까요? {money - 3000}원")
  else:
    print("걸어서 고고씽")
elif 2000 <= money:
  print("7800번 타고 고고씽")
  print(f"얼마남았나요? {money - 1000}원")
else:
  print("걸어서 고고씽")


'''
  도진이가 택시에 내려서 걸어서 귀가하던 중, 
  집 근처 오락실에서 '철권'게임을 하고 싶어졌습니다.
  회당 500원인 이 게임을 몇 번이나 할 수 있을까요?
  매번 게임을 진행한 뒤 도준이가 가지고 있는 잔액과 몇 번 게임을 했는지 횟수를 출력하는 코드를 작성하시오.

  현재까지의 게임한 횟수는 :
  현재 잔액 :

  최종 게임 횟수 :
  최종 잔액 :

'''

money = 7300
counts = 0
while True:
  counts += 1
  money -= 500
  print(f"현재까지의 게임한 횟수는 : {counts}" )
  print(f"현재 잔액 : {money}" )
  if money < 500:
    break
print(f"최종 게임 횟수 :{counts} ")
print(f"최종 잔액 : {money}")


