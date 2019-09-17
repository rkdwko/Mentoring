# X 와 Y 의 상관관계를 분석하는 기초적인 선형 회귀 모델을 만들고 실행해봅니다.
import tensorflow as tf

x_data = [1, 2, 3]
y_data = [1, 2, 3]

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

# name: 나중에 텐서보드등으로 값의 변화를 추적하거나 살펴보기 쉽게 하기 위해 
# 이름을 붙여줌.
X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")
print(X)
print(Y)

# X 와 Y 의 상관 관계를 분석하기 위한 가설 수식을 작성 .
# y = W * x + b
# W 와 X 가 행렬이 아니므로 tf.matmul 이 아니라 기본 곱셈 기호를 사용
hypothesis = #TODO

# 손실 함수를 작성
# mean(h - Y)^2 : 예측값과 실제값의 거리 : 비용(손실) 함수
cost = tf.reduce_mean(tf.square(hypothesis - Y))

#경사 하강법 최적화를 수행
optimizer = #TODO

# 비용을 최소화 하는 것이 최종 목표
train_op = #TODO

# 세션을 생성하고 초기화
with #TODO
    sess.run(tf.global_variables_initializer())

    # 최적화를 100번 수행
    for step in range(100):
        # sess.run 을 통해 train_op 와 cost 계산합니다.
        _, cost_val = sess.run([#TODO ], feed_dict={X: x_data, Y: y_data})

        print(step, cost_val, #TODO , #TODO  )

    # 최적화가 완료된 모델에 테스트 값을 넣고 결과가 잘 나오는지 확인해봅니다.
    print("\n=== Test ===")
    print("X: 5, Y:", sess.run(#TODO  ))
    print("X: 2.5, Y:", sess.run(#TODO  ) )
