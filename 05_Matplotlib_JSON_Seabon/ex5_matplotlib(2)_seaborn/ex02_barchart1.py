import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

#한글 폰트 등록
#font_location = "c:/Windows/fonts/malgun.ttf"
font_location = '/Macintosh HD/시스템/라이브러리/Fonts/AppleSDGothicNeo.ttc'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

animals = ('고양이', 'dog', 'rabbit', 'horse')
nums = (1, 2, 3, 4)

plt.figure()
plt.subplot(2,1,1)
plt.bar(animals, nums)

plt.subplot(2,1,2)
plt.barh(animals, nums)
plt.show()



