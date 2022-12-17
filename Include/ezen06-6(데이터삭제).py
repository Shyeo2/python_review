import pandas as pd
'''
    1. 데이터 삭제 : drop()
      - 필요한 데이터 삭제 
      - 행(index), 열(column)단위로 삭제

    2. 중복 데이터 삭제 : 
      - duplicated() : 데이터 중복 여부를 True, False 로 반환
                       keep: 중복이 있다면 처음과 마지막 값 중 어떤것을 중복이라고 판단 
      - drop_duplicates() : 중복된 데이터를 삭제
                            keep: 중복이 있따면 처음과 마지막 값 중 어떤것을 삭제
'''
df = pd.DataFrame({
  'SIZE' : ['L', 'M', 'L', 'S', 'XS'],
  'product_type' : ['Jacket', 'Shirt', 'Jacket', 'Trousers', 'Shirt'],
  'color' : ['red', 'black', 'black', 'red', 'blue'],
  'quantity' : [5, 15, 10 ,20 ,15]
})

print(df)
print()
print(df.drop(['color'], axis=1))

print()
print(df.drop(['color','quantity'], axis=1))

print()
print(df.drop(['SIZE','product_type'], axis=1))

print()
print(df)
print()
print(df.drop([0],axis=0))

print()
print(df.drop([1,4]))

print()
print(df)

#처음 값이 중복
print()
print(df.duplicated(['product_type'], keep='first'))

#마지막 값이 중복 
print()
print(df.duplicated(['product_type'], keep='last'))

print()
print(df)

# 중복된 값 중 처음 나온 것이 출력되고 나중에 나온 값이 삭제됨 
print()
print(df.drop_duplicates(['product_type'], keep='first'))

print()
print(df)

print()
print(df.drop_duplicates(['product_type'], keep='last'))