from sklearn.linear_model import LinearRegression

x = [[10],[5],[9],[7]]       #공부시간 10시간   5시간, 9시간, 7시간
y = [[100],[50],[90],[77]]   #시험점수 100점    50점,  90점   77점

model = LinearRegression()

model = model.fit(x, y)
result= model.predict([[8]])

print(result)

