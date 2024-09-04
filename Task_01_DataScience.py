#----------------------------------------------------------#
#      DATA VISUALIZATION -CREATE BAR GRAPH / HISTOGRAM 
#----------------------------------------------------------#

#dataset1: API_SP.POP.TOTL.FE.ZS_DS2_en_csv_v2_3412369
#dataset2: API_SP.POP.TOTL.MA.ZS_DS2_en_csv_v2_3421325

import pandas as pd
import matplotlib.pyplot as plt

country = str(input("Enter the Country for which you want the data : "))

columns = ['Country Name','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']
countries = ['Country Name']

data1 = pd.read_csv('F:/Prodigy_Projects/Task1/dataset1/dataset1.csv')
data2 = pd.read_csv('F:/Prodigy_Projects/Task1/dataset2/dataset2.csv')

df1 = pd.DataFrame(data1, columns=columns)
df2 = pd.DataFrame(data2, columns=columns)

df3 = pd.DataFrame(data1, columns=countries)

df3.to_csv('countries.csv')

#df.drop('Country Code', axis=1)
#df.drop('Indicator Name', axis=1)
#df.drop('Indicator Code', axis=1)

df1 = df1.set_index("Country Name")
df2 = df2.set_index("Country Name")
#set the type to int:

df1 = df1.astype(float)
df2 = df2.astype(float)
#plot an individual row with something like:

row1 = df1.loc[country]
plot1 = row1.plot(kind='line', xlabel = 'Years', ylabel='Percentage', title = 'Population of Australia in Percentage vs Years', color='red')

row2 = df2.loc[country]
plot2 = row2.plot(kind='line', xlabel = 'Years', ylabel='Percentage', title = 'Australias Population of Men and Women in Percentage vs Years', color='blue')
plt.legend(["Women","Men"], title = 'Index')

#df = pd.DataFrame(data, columns=['Country Name','Country Code','Indicator Name','Indicator Code'])

#df.to_csv('tmp1.csv')

#print(data.sort_values(by='Country Code')) 