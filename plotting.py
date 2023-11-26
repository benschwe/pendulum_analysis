from matplotlib import pyplot as plt
import pandas as pd
import os
import csv

file_name = '11-25-2023_09-06-28_log.csv'
with open(os.path.join(os.getcwd(), 'logs', file_name), 'r') as f:
  reader = csv.reader(f)
  data = [row for row in reader]
  data.pop(0)

new_file_name = file_name[:-4] + '_fixed_' + '.csv'
with open(os.path.join(os.getcwd(), 'logs', new_file_name), 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(data)

data = pd.read_csv(os.path.join(os.getcwd(), 'logs', new_file_name), delimiter='\t')

data.columns = (['Time (s)', 'Motor Angle', 'Motor Vel', 'Pend Angle Constrained', 'Pend Angle Corrected',
'Pend Vel', 'Target Current', 'Ready For Upright', 'Upright', 'Got Knockeddown', 'Motor Current Limit'])


data['Time (s)'] = data['Time (s)'] - data['Time (s)'].iloc[0]

fig, ax = plt.subplots(3, 1, sharex=True, figsize=(12,8))
ax[0].plot(data['Time (s)'], data['Pend Angle Corrected'], '-o', markersize=2)
ax[1].plot(data['Time (s)'], data['Pend Vel'], '-o', markersize=2)
ax[2].plot(data['Time (s)'], data['Motor Vel'], '-o', markersize=2)

plt.show()