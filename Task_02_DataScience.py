#---------------------------------------------------#
#              EXPLORATORY DATA ANALYSIS
#---------------------------------------------------#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from datetime import date
warnings.filterwarnings('ignore')

#Reading the data-set
data = pd.read_csv(r'C:/Users/ABC/Desktop/Prodigy Internship/Data Science/gender_submission.csv')
print("This will display the top5 observation in data set\n", data.head())
print("This will display the bottom5 observation in data set\n" ,data.tail())
print(data.info())
print(data.nunique())
#missing values
a = data.isnull().sum()
print(a)
#There are no missing values in the following dataset
#Now calculating the percentage of missing values
b = data.isnull().sum()/(len(data))*100
print(b)
#So, we don't get the result
#Atlast we are doing summmary of the following data
c = data.describe().T
d = data.describe(include='all').T