import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind


gender_data = pd.read_csv('C:/Users/cphil/Documents/GitHub/MATH495/genderRegressionData.csv')

"""
gender_data.info()
print(gender_data['gender'].corr(gender_data['Calories']))
print(gender_data['gender'].corr(gender_data['Fat (g)']))
print(gender_data['gender'].corr(gender_data['Saturated Fat (g)']))
print(gender_data['gender'].corr(gender_data['Sodium (mg)']))
print(gender_data['gender'].corr(gender_data['Total Carbohydrates (g)']))
print(gender_data['gender'].corr(gender_data['Sugars (g)']))
print(gender_data['gender'].corr(gender_data['Protein (g)']))
"""

female = gender_data[gender_data['gender'] == 1]
male = gender_data[gender_data['gender'] == 2]
maleAverage = {}

print(maleAverage)
print(female['Calories'].var())
print(male['Calories'].var())

print(ttest_ind(female['Calories'], male['Calories'], equal_var = False))

sns.scatterplot(x = 'USERID', y = 'Calories', data = female)
sns.scatterplot(x = 'USERID', y = 'Calories', data = male)
plt.show()
