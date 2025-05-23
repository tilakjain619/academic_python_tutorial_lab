#Load a dataset using pandas, perform basic data manipulation opertions(e.g. filtering, sorting, grouping), and save the modified dataset to a new file.

import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

filtered_data = data[data['total_bill'] > 20]

sorted_data = filtered_data.sort_values('total_bill')

grouped_data = sorted_data.groupby('day')[['total_bill', 'tip']].mean()

final_data = grouped_data.reset_index()

final_data.to_csv('new_file.csv', index=False)