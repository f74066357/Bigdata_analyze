#!/usr/bin/env python
# coding: utf-8

# In[1]:


spark


# In[2]:


sc.master


# In[3]:


get_ipython().system('hdfs dfs -ls')


# In[4]:


ls


# In[5]:


# !wget https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2018-10.csv


# In[6]:


get_ipython().system('cat yellow_tripdata_2018-10.csv | head -5')


# In[7]:


get_ipython().system('ls')


# In[8]:


get_ipython().system('hdfs dfs -put yellow_tripdata_2018-10.csv /hw3/input/')


# In[9]:


get_ipython().system('hdfs dfs -ls /hw3/input')


# In[21]:


from pyspark import SparkContext
from pyspark import SparkConf
import pyspark.sql.functions as F

conf = SparkConf()         .setAppName("Q2") 
sc = SparkContext.getOrCreate();

df = spark.read.csv('/hw3/input/yellow_tripdata_2018-10.csv',sep=',',header=True,inferSchema=True)
df.show(5, False)


# In[22]:


df.printSchema()


# In[23]:


from pyspark.sql.functions import desc
dfg=df.groupby('passenger_count').count().sort(desc("count"))
dfg.show(10)


# In[24]:


total= df.count()
total


# In[25]:


#expect passenger_count=0
total-106166


# In[26]:


avg=(6301766*1+1283324*2+373592*5+366264*3+226545*6+163341*4+44*7+34*8+29*9)/8714939
avg


# In[27]:


6301766/8821105


# In[43]:


# 用1來補passenger count=0


# In[53]:


# replace the missing values in passenger_count with 1.
dfnew = df.withColumn("passenger_count", F.when((df["passenger_count"] == "0"), 1).otherwise(df["passenger_count"]))


# In[54]:


dfgnew=dfnew.groupby('passenger_count').count().sort(desc("count"))
dfgnew.show(10)


# In[45]:


#credit card
df1 = dfnew.filter(dfnew["payment_type"] == "1").select("passenger_count", "total_amount")
df1.show(5)


# In[46]:


average_amounts1 = df1.groupby('passenger_count').agg({"total_amount": "average"})
average_amounts1.show()


# In[47]:


df2 = dfnew.filter(df["payment_type"] == "2") .select("passenger_count", "total_amount")
df2.show(5)


# In[48]:


average_amounts2 = df2.groupby('passenger_count').agg({"total_amount": "average"})
average_amounts2.show(10)


# In[36]:


# 改用2來補passenger count=0


# In[55]:


# replace the missing values in passenger_count with 2.
dfnew = df.withColumn("passenger_count", F.when((df["passenger_count"] == "0"), 2).otherwise(df["passenger_count"]))
dfgnew=dfnew.groupby('passenger_count').count().sort(desc("count"))
dfgnew.show(10)


# In[56]:


#credit card
df1 = dfnew.filter(dfnew["payment_type"] == "1").select("passenger_count", "total_amount")
average_amounts1 = df1.groupby('passenger_count').agg({"total_amount": "average"})
average_amounts1.show()


# In[57]:


df2 = dfnew.filter(df["payment_type"] == "2") .select("passenger_count", "total_amount")
average_amounts2 = df2.groupby('passenger_count').agg({"total_amount": "average"})
average_amounts2.show(10)

