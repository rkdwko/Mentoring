import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.linspace(0, 14, 100) #1부터 14깢 100개의 숫자 생성하여 리스트로 반환

y1 = np.sin(x)
y2 = 2*np.sin(x+0.5)
y3 = 3*np.sin(x+1.0)
y4 = 4*np.sin(x+1.5)

plt.figure(figsize=(15,10))

plt.subplot(2,2,1)
plt.plot(x,y1, x,y2, x,y3, x,y4)

sns.set_style("dark")
plt.subplot(2,2,2)
plt.plot(x,y1, x,y2, x,y3, x,y4)

sns.set_style("whitegrid")
plt.subplot(2,2,3)
plt.plot(x,y1, x,y2, x,y3, x,y4)

plt.show()

