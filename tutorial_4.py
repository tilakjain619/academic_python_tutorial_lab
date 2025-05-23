#Consider dataset of your choice and implement different visualization techniques to represent data using python libraries.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

sns.countplot(x='Survived', data=df)
plt.show()

sns.histplot(df['Age'].dropna(), bins=20, kde=True)
plt.show()

sns.boxplot(x='Pclass', y='Age', data=df)
plt.show()

sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.show()

corr = df[['Age', 'Fare', 'Pclass', 'SibSp', 'Parch']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()