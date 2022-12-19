'''
  리스트 내 원소 중에서 가장 큰 값의 인덱스(위치)를 찾아서 반환하는 함수를 작성하시오.

  data = [7, 1, 5, 9, 3, 2, 4]
'''


# max() 함수 사용 
# print(max(data))
# print(data.index(max(data)))

def index_max(data):
  largest_index = 0
  for i in range(len(data)):
    # 더 큰 값을 찾은 경우 
    if data[largest_index] < data[i]:
      largest_index = i
  return largest_index

data = [7, 1, 5, 9, 3, 2, 4]
print(index_max(data))

'''
  특정한 값을 가지는 원소의 인덱스를 찾는 함수를 작성해 보시오.

  [3, 5, 7, 9], 2  ==> -1
  [3, 5, 7, 9], 7  ==> 2
  
  enumerate() : 리스트의 원소에 순서값을 부여해주는 함수 
'''
print()
list = [3, 5, 7, 9]
def enum(num):
  for x,y in enumerate(list):
    if y == num:
      return x
  return -1
  
print(enum(2))
print(enum(5))

'''
  하나의 자연수가 주었을 때, 소수인지 아닌지 판별하는 함수를 작성하시오.
  - 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수다.
'''
def datermine_prime(x):
  # 1이하인 경우 소수가 아님 
  if x <= 1:
    return False
  # 1과 자기 자신외의 자연수로 나누어 지면 소수가 아님 
  for divisor in range(2, x):
    if divisor == 0:
      return False
  return True

print(datermine_prime(1))


