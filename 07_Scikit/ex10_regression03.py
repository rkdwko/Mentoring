from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

boston = load_boston()
dfX = pd.DataFrame(boston.data, columns=boston.feature_names)
dfy = pd.DataFrame(boston.target, columns=["MEDV"])
df = pd.concat([dfX, dfy], axis=1)
print( df.head())

"""
1978 보스턴 주택 가격 (MEDV)
506 타운의 주택 가격 중앙값 (단위 1,000 달러)

( 특징 데이터 ) 
CRIM: 범죄율
INDUS: 비소매상업지역 면적 비율
NOX: 일산화질소 농도
RM: 주택당 방 수
LSTAT: 인구 중 하위 계층 비율
B: 인구 중 흑인 비율
PTRATIO: 학생/교사 비율
ZN: 25,000 평방피트를 초과 거주지역 비율
CHAS: 찰스강의 경계에 위치한 경우는 1, 아니면 0
AGE: 1940년 이전에 건축된 주택의 비율
RAD: 방사형 고속도로까지의 거리
DIS: 직업센터의 거리
TAX: 재산세율
"
"""

"""
<데이터에 대한 사전 조사 >  
데이터에 누락된 값이 있는지 확인
각 데이터가 연속적인 실수값인지 범주형 값인지 확인
실수형 데이터의 분포가 정규 분포인지 확인
실수형 데이터에 양수 혹은 범위 등으로 제한 조건이 있는지 확인
범주형 데이터의 경우 범주의 값이 어떤 값 혹은 숫자로 표현되어 있는지 확인
데이터간의 상관관계를 확인
데이터에 이상한 값(outlier)들이 있는지 확인 
"""

cols = ["MEDV", "RM", "LSTAT", "NOX"]
sns.pairplot(df[cols])
plt.show()

"""
가격(MEDV)과 RM 데이터가 강한 양의 상관관계, 
LSTAT, NOX 데이터와 강한 음의 상관관계 
"""
data = df[[ "RM","LSTAT","NOX"]]
label = df["MEDV"]

model  = LinearRegression()
model  = model.fit(data, label)

#TODO   RM(방 수):6개,   LSTAT:9.67,   NOX: 0.573 일 때  집값을 예측해 보세요.
predict = model.predict([[6, 9.67, 0.573]])
print("예측 집값 : ", predict)

