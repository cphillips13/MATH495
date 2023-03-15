import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, normaltest, ranksums

gender_data = pd.read_csv('C:/Users/cphil/Documents/GitHub/MATH495/genderRegressionData.csv')
print(gender_data)
female = gender_data[gender_data['gender'] == 1]
male = gender_data[gender_data['gender'] == 2]
sns.scatterplot(x = 'USERID', y = 'Calories', data = female)
sns.scatterplot(x = 'USERID', y = 'Calories', data = male)
plt.show()

print(female)