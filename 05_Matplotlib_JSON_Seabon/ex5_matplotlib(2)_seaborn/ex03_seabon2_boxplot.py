import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("iris") # seaborn 팩키지의 샘플 데이터
print( tips.head(5) )

plt.figure(figsize=(10,10))


sns.set_style("whitegrid")
plt.subplot(2,2,1)
sns.boxplot(x=tips["sepal_width"])


plt.subplot(2,2,2)
sns.boxplot(x="species", y="sepal_width", data=tips)

plt.subplot(2,2,3)
sns.boxplot(x="species", y="sepal_width",hue="species", data=tips)
plt.show()

