# 기본 반복문 (while, for)
v1 = 1

while v1 < 11:
  print("v1 is :" , v1)
  v1 += 1

print()

for v2 in range(10):
  print("v2 is ", v2)

print()

for v3 in range(1, 11):
  print("v3 is :", v3)

# 2씩 증가 
for v4 in range(1, 11, 2):
  print("v4 is :", v4)

print()

# 1~ 100까지 합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
  sum1 += cnt1
  cnt1 += 1

print("1~ 100 합 :", sum1)
print("1~ 100 합 :", sum(range(1, 101)))
print("1~ 100안에 3의 배수의 합 :", sum(range(0, 101 , 3)))
for v5 in range(0, 101 , 3):
  print(v5)


# 시퀀스 (순서가 있는) 자료형
# 문자열, 리스트, 튜플 , 사전, 집합
# iterable 리턴함수 : range(), reversed(), enumerate(), filter(), map()....

#1
names = ["Ezen1", "Ezne2", "Ezen3", "Ezne4", "Ezne5", "Ezen6"]

for name in names:
  print("You are ", name)

print()

#2 
word = 'dreams'
for s in word:
  print("word : ", s)

#3 
my_info = {
  "name" : "SunHye",
  "age" : 28,
  "city" : "Suwon"
}

#key
for key in my_info:
  print(key, ":" , my_info[key])

#value
for val in my_info.values():
  print(val)
  
#key, value : items()
for key, val in my_info.items():
  print(key, val)

print()

#4
name = "Sunhye"

for n in name:
  if n.isupper(): 
    print(n.lower())
  else:
    print(n.upper())

