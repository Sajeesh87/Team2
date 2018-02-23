#import libraries
import pandas as pd

#importing dataset
dataset_train = pd.read_csv('train.csv')
print(dataset_train)

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
print(dataset_train.shape)
dataset_train.head()

f1 = dataset_train['V1'].values
f2 = dataset_train['V2'].values
X = np.array(list(zip(f1, f2)))
plt.scatter(f1, f2, c='black', s=7)