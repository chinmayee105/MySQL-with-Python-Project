#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

db = mysql.connector.connect(host = "your_host",
                             username = "your_username", 
                             password = "your_password",
                             database = "your_database")

cur = db.cursor()


# #### 1. List all Mobile Brands available in the dataset

# In[3]:


query = """ select distinct Brands from  mobilecompany.mobile; """

cur.execute(query)

data = cur.fetchall()

data


# #### 2. Find the average price of mobiles for each brand.

# In[4]:


query = """ select Brands, AVG(Price) as 
            average_price FROM mobile
            GROUP BY Brands """

cur.execute(query)

query = cur.fetchall()

query


# #### 3.Retrieve the details of the most expensive mobile

# In[5]:


query = """ select * FROM mobile 
            ORDER BY Price DESC 
            Limit 1 """

cur.execute(query)

data = cur.fetchall()

data


# #### 4. Find the total number of mobiles for each brands

# In[6]:


query = """ select Brands, COUNT(*) as 
            total_mobile FROM mobile
            GROUP BY Brands ; """

cur.execute(query)

data = cur.fetchall()

df = pd.DataFrame(data, columns = ["Brands", "total_mobile"])

df


# #### 5. Get the brand with the highest average RAM

# In[7]:


query = """ select Brands, AVG(RAM_Storage) as 
            average_RAM FROM mobile
            GROUP BY Brands 
            ORDER BY average_RAM DESC
            LIMIT 1 ; """

cur.execute(query)

data = cur.fetchall()

data


# #### 6.List all models with battery capacity greater than 45000 mAh.

# In[8]:


query = """ select * FROM mobile
            WHERE Battery_Capacity > 4000 """

cur.execute(query)

data = cur.fetchall()

data


# #### 7.Find the Brand with the cheapest average price

# In[9]:


query = """ select Brands, AVG(Price) as 
            average_price FROM mobile
            GROUP BY Brands 
            ORDER BY average_price ASC
            LIMIT 1 ; """

cur.execute(query)

data = cur.fetchall()

data


# #### 8.Get the models that have atleast 128GB of storage and 6GB of RAM

# In[10]:


query = """ select * FROM mobile
            WHERE Internal_Storage >= 128 AND RAM_Storage >= 6; """

cur.execute(query)

data = cur.fetchall()

data


# #### 9.How Does the number of mobile phones by brand correlate with their average price?

# In[11]:


query = """ select Brands, AVG(Price) AS
            average_price, COUNT(*) AS
            count FROM 
            mobile
            GROUP BY Brands"""

cur.execute(query)

data = cur.fetchall()

df = pd.DataFrame(data, columns = ['Brands','average_price','count'])
sns.lineplot(x = 'count', y = 'average_price', data = df)
plt.title('Correlation between number of phones and average price')
plt.show()


# #### 10.How does the number of mobile phones by Brand Correlate with their Average Price?

# In[12]:


query = """ select Brands, AVG(Internal_Storage) AS
            average_storage FROM mobile
            GROUP BY Brands"""

cur.execute(query)

data = cur.fetchall()

df = pd.DataFrame(data, columns = ['Brands','average_price'])
sns.barplot(x = 'Brands', y = 'average_price', data = df)
plt.title('Average Storage Capacity by Brand')
plt.xticks(rotation = 90)
plt.show()


# #### 11.What is the Distribution of Rating Accross all mobile phones?

# In[13]:


query = """ select price FROM 
            mobile"""

cur.execute(query)

data = cur.fetchall()

df = pd.DataFrame(data, columns = ['Price'])
sns.histplot(df['Price'], bins=30)
plt.title('Distribution of Mobile Phone Prices')
plt.xticks(rotation = 90)
plt.show()


# In[ ]:




