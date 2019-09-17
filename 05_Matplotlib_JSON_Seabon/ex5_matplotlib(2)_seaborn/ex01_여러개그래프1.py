import matplotlib.pyplot as plt

plt.figure()
plt.subplot(2,1,1)  #2행 1열 그래프의 첫번째 그래프
plt.plot([1,2,3,4],[1,2,3,4])

plt.subplot(2,1,2)  #2행 1열 그래프의 두번째 그래프
plt.plot([1,2,3,4],[2,4,8,4])
plt.show()

