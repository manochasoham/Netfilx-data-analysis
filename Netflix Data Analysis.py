#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import library 
import pandas as pd 

data=pd.read_csv(r"C:\Users\saksh\Downloads\8. Netflix Dataset.csv")
data


# In[2]:


# getting some basic infomation

# to show top 5 record from datasets
data.head()


# In[3]:


# to show bottom 5 record from datasets

data.tail()


# In[4]:


# to show no. of rows and columns 

data.shape


# In[5]:


# to show no. of total values inn datasets 

data.size


# In[6]:


# to show how many columns in datasets 

data.columns


# In[7]:


# to show the data type 
data.dtypes


# In[8]:


# to show the dataset information
data.info()


# In[9]:


# task 1 

# find duplicate

data[data.duplicated()]


# In[10]:


# remove duplicate data from datasets 
data.drop_duplicates(inplace=True)


# In[11]:


#  rechecking duplicates  
data[data.duplicated()]


# In[12]:


# checking null values
data.isnull()


# In[13]:


data.isnull().sum() # sum the column wise null


# In[14]:


# import library to show null values through heatmap
import seaborn as sns
sns.heatmap(data.isnull())


# In[15]:


# what is the show id and the director of the "house of cards "

data[data['Title'].str.contains("House of Cards")] # 1 method


data[data['Title'].isin(["House of Cards"])] # 2 method


# In[16]:


# In which year highest number of movies and series were release ? 

import datetime  as dt
data['date_no']=pd.to_datetime(data['Release_Date'])
# print(data.dtypes)

data['date_no'].dt.year.value_counts() # it counts number of occurence 


# In[17]:


data['date_no'].dt.year.value_counts().plot(kind='bar') # show the values through bar graph


# In[18]:


# counts the category in datasets 

# data.head(2)Permalink


sns.countplot(data['Category']) # to show count of tv shows and movies 


# In[19]:


# find the movies which are release in 2020 

data['year']=data['date_no'].dt.year
data.head(2)


# In[20]:


data[(data['Category']=="Movie") & (data['year']==2020)]


# In[21]:


# show the title of all tv shows that were release in india  

data[(data['Category']=="TV Show") & (data['Country']=='India')]


# In[22]:


#  To show top 10 director , who gave top numbers of movies and tv shows 

data['Director'].value_counts().head(10)


# In[23]:


# what are the different rating defined by the netflix?


data['Rating'].nunique() # checking how many unique rating 
data['Rating'].unique() # name of unique values 


# In[24]:


# how many movie got the R rating in india 
data.head(1
         )

(data['Category']=="Movie")


# In[25]:


# how many movies got R rating in india 

data[(data['Category']=='Movie')& (data['Rating']=="R")& (data['Country']=="India")]


# In[43]:


# checking rating  growth 
data['Rating'].value_counts().plot(kind='area')


# In[69]:


# which country has the highest number of tv show 

data_tv_show=data[data['Category']=="TV Show"]
data_tv_show.Country.value_counts()
show=data_tv_show.head(6)


# In[66]:


show.Country.value_counts().plot(kind="bar")


# In[ ]:




