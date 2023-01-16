'''
    1. 딥러닝 모델의 학습 과정

        데이터 준비 ==> 모델 (모형) 정의
                            ↓
                      모델 (모형) 컴파일     ←   옵티마이저(optimizer)선택, 손실함수(loss)선택
                            ↓
                      모델 (모형) 학습(훈련)
                            ↓
                      모델 (모형) 평가

    2. 텐서플로 (TensorFlow)
        - 기계 학습 프레임워크(framework) 중 하나임.
            - 텐서(tensor)를 Numpy 배열처럼 사용할 수 있음
            - 데이터 흐름 그래프(data flow graph)를 사용하여 데이터의 수치연산을 하는 오픈 소스 소프트웨어 프레임워크
            - 넘파이 같은 다양한 라이브러리를 묶어 놓은 패키지라고도 할 수 있음
        - Tensorflow를 사용하면 , GPU 연동을 통해 효율적으로 딥러닝 모델을 학습할 수 있음
        - google Colab을 이용하면 , 손쉽게 Tensorflow를 시작할 수 있음
        - 텐서플로에서 데이터의 수치 연산을 수행하기 위한 그래프
            - 그래프의 노드(node)는 수학적 연산을 처리하고,
            - 에지(edge)는 노드 사이의 관계를 표현하며, 데이터(tensor) 이동을 수행

    3. 벡터, 행렬, 텐서
        - 인공지능(머신러닝/딥러닝)에서 데이터는 벡터(Vector)로 표현
        - 벡터는 [1.0, 1.1, 1.2]처럼 숫자들의 리스트로, 1차원 배열 형태
        - 행렬(matrix)은 행과 열로 표현되는 2차원 배열 형태
        - 텐서는 3차원 이상의 배열 형태
            [[1,2] [3,4]
             [5,6] [7,8]
                        ]

    4. 텐서플로 특징 및 장점
        1) 데스크톱, 서버 혹은 모바일 디바이스에서 코드 수정없이 CPU나 GPU를 사용하여 연산을 구동할 수 있음
        2) 분산(distributed) 환경에서 실행 가능
        3) 단순한 아이디어 테스트부터 서비스 단계까지 모두 이용 가능
        4) 자동으로 미분을 계산할 수 있음
            - 딥러닝 역전파 과정 오차를 최소화하고자 미분을 이용하여 가중치를 업데이트
        5) 텐서플로 2.x 부터는 데이터를 학습하고 예측하고 과정이 매우 단순해졌음
        6) 직관적이고 접근하기 쉬운 파이썬 인터페이스를 제공

'''
import os
import numpy as np
import tensorflow as tf

# 로그레벨이 3이 되면 warning이 뜨지 않음
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
'''
    길이가 100이고 shape가 (3,)인 1차원 배열을 생성한 후, (100,3)크기의 2차원 배열로 변환함 
'''
x = np.random.sample((100,3))
# print(x)
'''
    * GPU 사용 여부 체크하기
        - GPU를 사용하면 텐서플로우에게 딥러닝 모델을 더욱 효과적으로 사용할 수 있음 
'''
tf.debugging.set_log_device_placement(True)         # 각 텐서와 연산이 어떠한장치에 할당되었는지 출력하시
dataset = tf.data.Dataset.from_tensor_slices(x)
print(dataset)

a = tf.constant([
    [1,1],
    [2,2]
])

b = tf.constant([
    [5,6],
    [7,8]
])

c = tf.matmul(a,b)
print(c)

tf.debugging.set_log_device_placement(False)
print(c)