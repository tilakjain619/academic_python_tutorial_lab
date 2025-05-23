#Consider dataset of your own choice and implement employee salary analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['HR', 'IT', 'IT', 'Sales', 'HR'],
    'Salary': [55000, 80000, 75000, 60000, 50000],
    'Experience': [3, 5, 4, 2, 1]
}

df = pd.DataFrame(data)

average_salary = df['Salary'].mean()

plt.figure(figsize=(8, 5))
sns.barplot(x='Employee', y='Salary', data=df)
plt.title('Employee Salary')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x='Department', y='Salary', data=df)
plt.title('Salary Distribution by Department')
plt.show()

salary_by_experience = df.groupby('Experience')['Salary'].mean()

plt.plot(salary_by_experience)
plt.title('Average Salary by Experience')
plt.xlabel('Experience (years)')
plt.ylabel('Average Salary')
plt.show()
