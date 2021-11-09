# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 00:44:25 2021

@author: USER
"""
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
#from scipy.stats import linregress

data= pd.read_csv("C:\\path.csv")
data.sort_values(by=['Age'],inplace=True)
df_exp_p= data[data["Phone Price"] > 2000]
frequency = df_exp_p[['Email', 'Web','Mobile','Walk-In','Video Call','Phone Call','Letter']].apply(pd.Series.value_counts)
maximum = frequency.idxmax(axis="columns")
print("The most preffered way of requesting for an interview is:",maximum.values)
#median_age = data['Age'].median()
#dfpo= data[data["Annual Income"]/12 >= 5000] 
#print(dfpo["Phone Owned"])


#dfmasters = data[data["Education"] == "Masters"] 
#dfdiploma = data[data["Education"] == "Diploma"]            
#masters_avg = dfmasters["Annual Income"].mean()
#diploma_avg = dfdiploma["Annual Income"].mean()
#average_salary_diff = diploma_avg - masters_avg
#print("median:",median_age)
#print("Average saray difference between Diploma holders and Master's Degree holders:",average_salary_diff)
'''
x = dfdiploma["Age"]
y = dfdiploma["Annual Income"]

stats = linregress(x, y)
m = stats.slope
c = stats.intercept
x_value = int(input("Enter Age:"))
y_value = m*x_value + c
#print (y_value)
plt.scatter(x, y)
plt.annotate('Annual Salary = RM%.1f'%(y_value),xy=(x_value,y_value), xytext=(x_value-2.5,y_value-4000),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.plot(x, m * x + c, color="red")   
plt.show()
'''



