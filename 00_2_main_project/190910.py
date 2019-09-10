import pandas as pd
import os
population = pd.read_table('C:/Users/709-000/Desktop/서울시 상권분석 데이터/서울시 우리마을 가게 상권분석서비스(상권-추종유동인구_원본)작업.txt',sep=';')

list(population.columns)

population2014 = population[population['stdr_yy_cd'] == 2014]
population2015 = population[population['stdr_yy_cd'] == 2015]
population2016 = population[population['stdr_yy_cd'] == 2016]
population2017 = population[population['stdr_yy_cd'] == 2017]
population2018 = population[population['stdr_yy_cd'] == 2018]
population2019 = population[population['stdr_yy_cd'] == 2019]

population2014.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/유동인구2014.csv", mode='w')
population2015.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/유동인구2015.csv", mode='w')
population2016.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/유동인구2016.csv", mode='w')
population2017.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/유동인구2017.csv", mode='w')
population2018.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/유동인구2018.csv", mode='w')
population2019.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/유동인구2019.csv", mode='w')

list(population2018.columns)

population2018_test = population2018[['stdr_yy_cd', 'stdr_qu_cd', 'trdar_se_cd', 'trdar_se_cd_nm', 'trdar_cd', 'trdar_cd_nm', 'tot_flpop_co']]
population2018_test
population2018_test.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/유동인구2018test.csv", mode='w',encoding='euc-kr')


slae = pd.read_csv('C:/Users/709-000/Desktop/서울시 상권분석 데이터/서울시 우리마을가게 상권분석서비스(상권-추정매출).csv')
list(slae.columns)


slae2018 = slae[slae["기준_년_코드"]==2018]

list(slae2018.columns)
slae2018_test = slae2018[['기준_년_코드', '기준_분기_코드', '상권_구분_코드', '상권_구분_코드_명', '상권_코드', '상권_코드_명', '서비스_업종_코드', '서비스_업종_코드_명','당월_매출_금액','점포수']]

slae2018_test.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/매출2018test.csv", mode='w', encoding=utf-8)

slae2014.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/매출2014.csv", mode='w')
slae2015.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/매출2015.csv", mode='w')
slae2016.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/매출2016.csv", mode='w')
slae2017.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/매출2017.csv", mode='w')
slae2018.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/매출2018.csv", mode='w')
slae2019.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/매출2019.csv", mode='w')

----------------------------------------------------



list(slae2018.columns)

industry = pd.read_table('C:/Users/709-000/Desktop/서울시 상권분석 데이터/서울시 우리마을가게 상권분석서비스(상권영역).csv',sep=',')
industry.columns
industrytest = industry[['상권_구분_코드', '상권_구분_코드_명', '상권_코드', '상권_코드_명','시군구_코드', '행정동_코드']]

industrytest.to_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/상권영역.csv", mode='w')

----------------------------------------------------------

sang = pd.read_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/상권영역.csv")
popu = pd.read_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/유동인구2018test.csv")
sale = pd.read_csv("C:/Users/709-000/Desktop/유동인구, 매출 분할/매출2018test.csv")

popu1.columns
popu1 = popu.groupby('trdar_cd').mean()
del popu1['Unnamed: 0']
popu1 = popu1.reset_index()
del popu1['stdr_yy_cd']
del popu1['stdr_qu_cd']


sale1.columns
sale1 = sale.groupby(['상권_코드','서비스_업종_코드']).mean()
sale1 = sale1.reset_index()
del sale1['Unnamed: 0']
del sale1['기준_년_코드']
del sale1['기준_분기_코드']

del sang['Unnamed: 0']

popu1.columns
sale1.columns
sang.columns

popu1 = popu1.rename(columns = {'trdar_cd':'상권_코드'})
sale1 = sale1.rename(columns = {'trdar_cd':'상권_코드'})

po_merge = pd.merge(popu1,sang, on = '상권_코드')
sa_merge = pd.merge(sale1,sang, on = '상권_코드')

po_merge.columns
sa_merge.columns


su_merge  = pd.merge(po_merge,sa_merge, on = ['상권_코드','행정동_코드'])
su_merge1.columns

su_merge1 = su_merge[['상권_코드','상권_코드_명_x','시군구_코드_x','행정동_코드','서비스_업종_코드','tot_flpop_co','점포수', '당월_매출_금액','상권_구분_코드_x','상권_구분_코드_명_x']]
su_merge1['유동업종'] =  (su_merge1['tot_flpop_co']/su_merge1['점포수'])



ai = []
for i in set(su_merge1['서비스_업종_코드']):
    temp = su_merge1[su_merge1['서비스_업종_코드']==i]
    ai.append(temp)
range(len(ai))

import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np


c.columns
d = c.replace([np.inf, -np.inf], np.nan)
d.dropna()
model = smf.ols(formula = '유동업종 ~ tot_flpop_co', data = d).fit()
model.summary()


import matplotlib.pyplot as plt
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns

sns.lmplot('tot_flpop_co', '유동업종', data = d)
plt.show()


sns.lm

plot(model)
model.plt
model.fit(tot_flpop_co, 유동업종)

























