'''
    7) 텐서의 연산
        - 텐서에 대하여 사칙연산

    8) 텐셔의 평균 함수
        - 텐서플로우에서는 차원이 감소한다는 의미로 reduce라는 용어를 사용함
        텐서의 합계 함수
        텐서의 최대 함수
        - max() : 원소의 최대값 반환
        텐서의 차원 줄이기 혹은 늘리기
            - unsqueeze()
                - 크기가 1인 차원을 추가힘
            - squeeze()
                - 크기가 1인 차원을 제거함

    9) 자동 미분과 기울기 (gradient)
        - TensorFlow에서는 Gradient Tape 기능을 제공
        - "기울기 테이프"라는 의미를 가짐
        - 중간의 관련 연산들을 테이프에 기록하고, 역전파를 수행했을 때 기울기가 계산됨

'''



import os
import numpy as np
import tensorflow as tf

# 로그레벨이 3이 되면 warning이 뜨지 않음
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# 기본적으로 요소별 연산
a = tf.constant([
    [1, 2],
    [3, 4]
])

b = tf.constant([
    [5, 6],
    [7, 8]
])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print("-------------------------------------------------------------")

# 행렬 곱 (matrix multiplication)
print(tf.matmul(a, b))
print("-------------------------------------------------------------")

a = tf.constant([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print(a)
print(tf.reduce_mean(a))                # 전체 원소에 대한 평균
print(tf.reduce_mean(a, axis=0))        # 각 열에 대하여 평균 계산
print(tf.reduce_mean(a, axis=1))        # 각 행에 대하여 평균 계산

print("-------------------------------------------------------------")
print(tf.reduce_sum(a))                 # 전체 원소에 대한 평균
print(tf.reduce_sum(a, axis=0))         # 각 열에 대하여 합계 계산
print(tf.reduce_sum(a, axis=1))         # 각 행에 대하여 합계 계산

print("-------------------------------------------------------------")
print(tf.reduce_max(a))                 # 전체 원소에 대한 최대값
print(tf.reduce_max(a, axis=0))         # 각 열에 대하여 최대값 계산
print(tf.reduce_max(a, axis=1))         # 각 행에 대하여 최대값 계산

print("-------------------------------------------------------------")
print(tf.argmax(a, axis=0))             # 각 열에 대하여 최대값의 인덱스 계산
print(tf.argmax(a, axis=1))             # 각 행에 대하여 최대값의 인덱스 계산

print("-------------------------------------------------------------")
print(a)

print("첫번째 축-------")
# 첫번째 축에 차원 추가 (2차원 → 3차원)
a = tf.expand_dims(a, 0)
print(a.shape)
print(a)

print("네번째 축-------")
# 네번째 축에 차원 추가
a = tf.expand_dims(a, 3)
print(a.shape)
print(a)
print("-------")
# 크기가 1인 차원 제거
a = tf.squeeze(a)
print(a)
print(a.shape)






