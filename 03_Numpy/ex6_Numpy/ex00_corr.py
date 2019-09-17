import pandas as pd
lst = [[1,2,3,4,5,6,7],
 [10,15,20,25,50,55,60],
 [0,0,0,0,0,0,0],
 [-1,-20,-30,-45,-50,-55,-70]]
df = pd.DataFrame(lst).T
#TODO
df = pd.DataFrame(lst).T
corr = df.corr(method = 'pearson')
print(corr)