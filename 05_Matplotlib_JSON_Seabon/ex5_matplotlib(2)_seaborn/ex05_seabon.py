import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("iris")  # seaborn 팩키지의 샘플 데이터

sns.set(style="ticks")
iris = sns.load_dataset("iris")

sns.pairplot(iris)
plt.show()

sns.pairplot(iris, hue="species")
plt.show()

sns.pairplot(iris, vars=["sepal_width", "sepal_length"])
plt.show()

sns.pairplot(iris, x_vars=["sepal_width", "sepal_length"],
             y_vars=["petal_width", "petal_length"])
plt.show()

