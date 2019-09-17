from sklearn.linear_model import LinearRegression

x = [[10,3],[5,2],[9,3],[7,3]]      #공부시간,학년: 10시간,3   5시간,2, 9시간,3, 7시간,3
y = [[100],[50],[90],[77]]          #시험점수:      100점      50점,    90점      77점

model = LinearRegression()

model = model.fit(x,y)
result = model.predict([[7, 2]])
#TODO  #7시간공부,  2학년

print(result)

