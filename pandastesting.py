import pandas as pd
import numpy as np
import matplotlib as plt

gender_data = pd.read_csv('C:/Users/cphil/Documents/GitHub/MATH495/genderRegressionData.csv')
gender_data.plot.scatter(x = 'S1', y = 'A2')
