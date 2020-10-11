#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_html('https://www.local10.com/news/local/2020/03/29/the-numbers-how-many-coronavirus-cases-in-my-city/')

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 5)
pd.set_option('display.width', 1000)

df = pd.DataFrame(data[0])
df = df.fillna(0)		# Replace NaN with 0.0
# df = df.drop([df.index[2], df.index[5]])  	# Drop unnecessary data
df = df.drop(df.index[0:6])  # Data drop for matplotlib
#df = df[:-1]		   	# Drop last row
df = df.reset_index(drop=True)  # Reset index

print(df)

df.iloc[:, 1] = df.iloc[:, 1].astype(int)  # Convert second column to integer format

df.plot(kind='barh', x=df.columns[0], y=df.columns[1]).invert_yaxis()

plt.title('South Florida COVID-19 Data')
plt.tight_layout()
plt.tick_params(axis='y', which='major', labelsize=7)
plt.show()
