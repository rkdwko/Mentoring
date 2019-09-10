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

popu.columns
del popu['Unnamed: 0']
del sale['Unnamed: 0']
popu1 = popu
popu1['trdar_cd2'] = popu1['trdar_cd']
popu1.columns

del sang['Unnamed: 0']

popu2 = popu1.groupby('trdar_cd').mean()
popu2.columns
del popu2['stdr_qu_cd']
popu2

del popu2['stdr_yy_cd']




sang.columns
popu2 = popu2.rename(columns = {'trdar_cd2':'상권_코드'})

popu2['상권_코드'].astype(int)
sang['상권_코드'].astype(int)

po_merge = pd.merge(popu2,sang, on = '상권_코드')

----------------------------------------------
sale.columns
sale1 = sale
sale1['상권_코드2'] = sale['상권_코드']

sale2 = sale.groupby(['상권_코드','상권_코드_명','서비스_업종_코드','서비스_업종_코드_명']).mean()
sale2.columns
del sale2['기준_년_코드']
del sale2['기준_분기_코드']
sale2 = sale2.rename(columns = {'상권_코드2':'상권_코드'})




