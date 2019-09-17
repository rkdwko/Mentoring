import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

mr = pd.read_csv("mushroom.csv", header=None)

label = []
data = []
attr_list = []

# data와 label로 나누고
# data 내부의 기호를 숫자로 변환하기  (fit함수의 학습 데이터는 숫자이거나 숫자로 형변환이 가능해야함)

for row_index, row in mr.iterrows(): #DataFrame객체 의 iterrows() 메소드를 for문과 함께 사용하면
                                     # 행인덱스와, 행데이터를  한행 씩 반환
    #label.append(row.ix[0]) #0번 컬럼에 독이 있는지 없는지 정보를 label리스트에 담는다.
    label.append(row.iloc[0]) #0번 컬럼에 독이 있는지 없는지 정보를 label리스트에 담는다.
    row_data = []
    #for v in row.ix[1:]:
    for v in row.iloc[1:]:
        row_data.append(ord(v)) #Return the Unicode code point for a one-character string.

    data.append(row_data)

# 학습 전용과 테스트 전용 데이터로 나누기
data_train, data_test, label_train, label_test = \
    train_test_split(data, label)

# 데이터 학습
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

# 데이터 예측
predict = clf.predict(data_test)

# 결과 테스트
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)

print("정답률 =", ac_score)
print("리포트 =\n", cl_report)



