import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

#한글 폰트 등록
font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

import pandas as pd
CCTV_Seoul = pd.read_csv("ex01_CCTV_in_Seoul.csv",encoding="utf-8")
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별' }, inplace=True)
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[1] : 'CCTV설치수_소계' }, inplace=True)

pop_Seoul = pd.read_excel('ex01_population_in_Seoul.xls',
                          header = 2,
                          usecols = 'B, D, G, J, N',
                          encoding='utf-8')

pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별',
                          pop_Seoul.columns[1] : '인구수',
                          pop_Seoul.columns[2] : '한국인',
                          pop_Seoul.columns[3] : '외국인',
                          pop_Seoul.columns[4] : '고령자'}, inplace=True)


data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')
print(data_result.head())

###################
plt.figure()
data_result['CCTV설치수_소계'].plot(kind='barh', grid=True, figsize=(10,10))
plt.show()

###################
data_result['CCTV설치수_소계'].sort_values().plot(kind='barh',
                                     grid=True, figsize=(10,10))
plt.show()

###################
data_result['CCTV비율'] = data_result['CCTV설치수_소계'] / data_result['인구수'] * 100
data_result['CCTV비율'].sort_values().plot(kind='barh',
                                         grid=True, figsize=(10,10))
plt.show()

###################
plt.figure(figsize=(6,6))
plt.scatter(data_result['인구수'], data_result['CCTV설치수_소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()
###################
