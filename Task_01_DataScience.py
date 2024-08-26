#----------------------------------------------------------#
#      DATA VISUALIZATION -CREATE BAR GRAPH / HISTOGRAM 
#----------------------------------------------------------#
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\ABC\\Desktop\\Python Programming\\Machine Learning\\data.csv')


#Now we will plot a histogram 
plt.figure(figsize=(8,6))
plt.hist(df['Volume'], bins=60, color='skyblue', edgecolor='black', width = 0.5)
plt.hist(df['Weight'], bins=60, color='skyblue', edgecolor='blue', width = 0.5)
plt.hist(df['CO2'], bins=60, color='skyblue', edgecolor='red', width = 0.5)

#Now adding labels
plt.xlabel('Volume, Weight & CO2')
plt.ylabel('Cars')
plt.title('Histogram of Cars Vs. Weight')
plt.show()
