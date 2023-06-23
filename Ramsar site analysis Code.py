#!/usr/bin/env python
# coding: utf-8

# import of different libraries 
# 1. Matplotlib
# 2. Pandas
# 3. Numpy

# In[10]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[ ]:





# Read csv File For Fund Data of Wetlands

# In[11]:


fund_data_frame=pd.read_csv("C:/Users/parth/OneDrive/Desktop//statewise fund data.csv")
fund_data_frame.head()


# In[ ]:





# Code to Plot Timeserise Data In Line Chart

# In[12]:


x=fund_data_frame['years']
y=fund_data_frame['Gujarat']
y1=fund_data_frame['Himachal Pradesh']
y2=fund_data_frame['Manipur']
y3=fund_data_frame['Orissa']

plt.figure(figsize=(12,2),dpi=200)

plt.plot(x,y,marker='.',markersize=5,label='Gujarat')
plt.plot(x,y1,marker='.',markersize=5,label='Himachal Pradesh')
plt.plot(x,y,marker='.',markersize=5,label='Jammu & Kashmir')
plt.plot(x,y2,marker='.',markersize=5,label='Manipur')
plt.plot(x,y3,marker='.',markersize=5,label='Orissa')

plt.title('selective statewise fund release for wetland conservation')
plt.xlabel('year')
plt.ylabel('Rupee(In Lakh)')
plt.legend()


plt.show()


# In[ ]:





# Read csv File For Data of Wetlands

# In[4]:


category_data_frame=pd.read_csv("C:/Users/parth/OneDrive/Desktop/new ramsar indiastat/Category-wise Wetlands Area 2011.csv")
category_data_frame.head()


# In[ ]:





# Code For Plotting Piechart

# In[5]:


category=category_data_frame['Wetland Category']
value=category_data_frame['Wetland Area (In %age)']
plt.figure(figsize=(5,5),dpi=200)
plt.pie(value,labels=category,explode=[0.05,0.05,0.05,0.05],shadow=True,startangle=90,autopct='%2.2f%%')
plt.title('category wise wetland distribution 2011')

plt.show()


# In[ ]:





# Read csv File For Data of Wetlands

# In[6]:


category_data_frame1=pd.read_csv('C:/Users/parth/OneDrive/Desktop/new ramsar indiastat/Category-wise Wetlands Area (2017-2018).csv')
category_data_frame1.head()


# In[ ]:





# Code For Plotting Piechart

# In[7]:


category1=category_data_frame1['Wetland Category']
value1=category_data_frame1['Wetland Area (In %age)']
plt.figure(figsize=(5,5),dpi=200)
plt.pie(value1,labels=category1,explode=[0.05,0.05,0.05,0.05],shadow=True,startangle=90,autopct='%2.2f%%')
plt.title('category wise wetland distribution 2017-18')
plt.show()


# In[ ]:





# Read csv File For Chronological areal Data of Wetlands

# In[8]:


wetland_data_frame=pd.read_csv("C:/Users/parth/OneDrive/Desktop/new ramsar indiastat/Wetlands data.csv")
wetland_data_frame.head()


# In[ ]:





# Code Plot Chronological areal Data in Multiple Bar Graph

# In[9]:


x=wetland_data_frame['State']
x1=wetland_data_frame['Wetland area (ha) 1994']
x2=wetland_data_frame['Wetland area (ha) 2005']
x3=wetland_data_frame['Wetland area (ha) 2016']
width=0.2
numbers=np.arange(len(x))
plt.figure(figsize=(19,10),dpi=200)
plt.bar(numbers,x1,width,label='1994')
plt.bar(numbers+width,x2,width,label='2005')
plt.bar(numbers+width+width,x3,width,label='2016')

plt.xlabel('States')
plt.ylabel('Area(Ha)')
plt.title('state wise change in wetland area')
plt.legend()
plt.xticks(numbers+0.1,x,rotation=80)

plt.show()


# Code Plot Chronological areal Data in Multiple Bar Graph

# In[14]:


fish_data_frame=pd.read_csv("C:/Users/parth/OneDrive/Desktop/new ramsar indiastat/marine in wetland.csv")
fish_data_frame.head()


# In[ ]:





# Code Plot Chronological areal Data in Multiple Bar Graph

# In[17]:


x=fish_data_frame['Year']
y1=fish_data_frame['Marine contribution (%)']
y2=fish_data_frame['In-land contribution (%)']
width=0.4
numbers=np.arange(len(x))
plt.figure(figsize=(6,5),dpi=200)
plt.bar(numbers,y1,width,label='Marine(%)')
plt.bar(numbers+width,y2,width,label='Inland(%)')

plt.xlabel('Year')
plt.ylabel('Percentage(%)')
plt.title('catagorical data on fishing')
plt.legend()
plt.xticks(numbers+0.1,x,rotation=80)

plt.show()


# In[ ]:




