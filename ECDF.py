import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

# Set up Tl's preferred set_ylabel
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

# 1. Function to compute ECDF
def ecdf(data):
    """compute x, y values for an empirical cumulative distribution function"""
    x = np.sort(data)
    y = np.arange(1, len(data)+1)/len(data)
    return x, y

#load in data
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')

# 3. Generate ECDFs
x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)


# 4. Plot ECDFs
fig, ax = plt.subplots(1,1)
_ = ax.set_xlabel('egg cross sectional area (µm$^2$)')
_ = ax.set_ylabel('ECDF')

# "paint" the data!
_ = ax.plot(x_high, y_high, marker='.', linestyle='none')
_ = ax.plot(x_low, y_low, marker='.', linestyle='none')
ax.legend(('high food', 'low food'), loc='lower right')

# Save the figure
fig.savefig('ECDF.pdf')

plt.show()
