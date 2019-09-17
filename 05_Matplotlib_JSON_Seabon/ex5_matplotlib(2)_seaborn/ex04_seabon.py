import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")  # seaborn 팩키지의 샘플 데이터

sns.set_style("darkgrid")
sns.lmplot(x="total_bill", y="tip", data=tips, size=7 ,)
plt.show()

sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips, size=7)
plt.show()

sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips, palette="Set1", size=7)
plt.show()