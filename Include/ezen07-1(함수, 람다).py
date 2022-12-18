# ezen07
# 파이썬 함수 및 람다(lamda)
'''
  1. 함수 정의
  def function_name(parameter):
    code
  2. 함수 호출
  function_name()
'''

# 함수1
def hello(world):
  print("Hello, ", world)

hello("NiceYear")

print()

# 함수2 (return)
def hello_return(world):
  value = "Hello," + str(world)
  return value

str = hello_return("Ezen!")
print(str)

# 함수3(다중리턴)
def func_mul(x):
  y1 = x * 2
  y2 = x * 4
  y3 = x * 6
  return y1, y2, y3

va11, val2, val3 = func_mul(3)
print(va11, val2, val3)

print()
# 튜플리턴
def func_mul2(x):
  y1 = x * 2
  y2 = x * 4
  y3 = x * 6
  return (y1, y2, y3)

tup = func_mul2(4)
print(type(tup), tup)

# 리스트 리턴 
def func_mul3(x):
  y1 = x * 2
  y2 = x * 4
  y3 = x * 6
  return [y1, y2, y3]

lis = func_mul3(6)
print(type(lis), lis, set(lis))

print()

# 딕셔너리 리턴 
def func_mul4(x):
  y1 = x * 2
  y2 = x * 4
  y3 = x * 6
  return {'ret1' : y1, 'ret2': y2, 'ret3':y3}

dic = func_mul4(8)
print(type(dic), dic, dic.get('ret3'), dic.items(), dic.keys(), dic.values())

print()
# 함수4 (*args, **kwargs)

# *args
def args_func(*args):   # 매개변수명 자유롭게 변경 가능 
  for i,v in enumerate(args):
    print('{}'.format(i), v, end=' ')
args_func('ezen')
print()
args_func('ezen', 'ezenit', 'seoul')

print()
# **kwargs
def args_func2(**kwargs):   # 매개변수명 자유롭게 변경 가능 
  for v in kwargs.keys():
    print('{}'.format(v), kwargs[v], end=' ')
args_func2(name1='lee')
print()
args_func2(name1='lee', name2='kim')
print
args_func2(name1='lee', name2='kim', name3='park')

print()
# 함수5 - 혼합
def func_ezen(arg_1, arg_2 , *args, **kwargs):
  print(arg_1, arg_2, args, kwargs)
func_ezen(10, 20)

print()
func_ezen(10, 20, 'snow', 'snow3', 'rain')


# 함수6 - 중첩함수
def nested_func(num):
  def func_in_func(num):
    print(num)
  
  print("In func")
  func_in_func(num + 100)

#func_in_func(1)
nested_func(1)

# 함수7 
def tot_length(word: str, num: int ) -> int:
    return len(word) * num 
print("hint function" , tot_length("Heavy snow falls in Seoul", 10))