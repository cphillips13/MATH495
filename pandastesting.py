import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, normaltest, ranksums
import numpy as np

gender_data = pd.read_csv('C:/Users/cphil/Documents/GitHub/MATH495/updatingDBSF.csv')
print(gender_data.info)

print(gender_data['A2'])

print(gender_data['MacroTotal'])
sns.scatterplot(x = gender_data['A2'], y = gender_data['MacroTotal'])
X4 = np.arange(0, 6000, .05)
Y1 = X4
plt.ylabel("Calculated Calories (From Macros)")
plt.xlabel("Reported Calories")
plt.plot(X4,Y1)
plt.show()

newDf = gender_data[gender_data['DiffMacroAndActual'] < 300]
sns.scatterplot(x = newDf['A2'], y = newDf['MacroTotal'])
plt.ylabel("Calculated Calories (From Macros)")
plt.xlabel("Reported Calories")
plt.plot(X4,Y1)
plt.show()

print(newDf.info)