# ezen06-4
'''
  5) 딕셔너리(Dictionary) 자료형
    - {key1:Value1, key2:Value2, key3:Value3,.........}
    - {'name' : 'Jessica', 'age' : 19}    타입이 다를 수 있음
    - stu = {'name' : ['Jisoo', 'Jennie', 'Rose', 'Lisa'], 'age' : {19. 15. 16. 20}}

    
'''
stu = {'name' : ['Jisoo', 'Jennie', 'Rose', 'Lisa'], 'age': [19, 15, 16, 20]}

print(stu)
print(type(stu))

stu['math'] = [50, 100, 70, 80]
print(stu)

del stu['math']
print(stu)

for key, value in stu.items():
  print(key, value)