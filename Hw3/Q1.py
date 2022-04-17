#!/usr/bin/env python
# coding: utf-8

# In[1]:


spark


# In[2]:


sc.master


# In[3]:


get_ipython().system('ls')


# In[4]:


get_ipython().system('hdfs dfs -mkdir hw3')


# In[5]:


get_ipython().system('hdfs dfs -mkdir /hw3/input')
get_ipython().system('hdfs dfs -mkdir /hw3/output')


# In[6]:


get_ipython().system('hdfs dfs -put Youvegottofindwhatyoulove.txt /hw3/input/')


# In[7]:


get_ipython().system('hadoop fs -cat /hw3/input/Youvegottofindwhatyoulove.txt')


# In[12]:


from pyspark import SparkContext
from pyspark import SparkConf
import time

sparkConf = SparkConf()         .setAppName("Q1") 
sc = SparkContext.getOrCreate();
#print sc.master

text_file = sc.textFile("/hw3/input/Youvegottofindwhatyoulove.txt")

# count how many sentences 
sum = text_file.flatMap(lambda x: x.split("."))
total=0
for w in sum.take(sum.count()):
    #print(w)
    if not w:
        #print('no')
        continue;
    else:
        total=total+1
print("Total sentences:"+str(total))

# count times for each word
counts = text_file.map( lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').replace('\'',' ').replace('\"',' ').lower())         .flatMap(lambda x: x.split())         .map(lambda x: (x, 1))         .reduceByKey(lambda x,y:x+y)         .map(lambda x:(x[1],x[0]))         .sortByKey(False)

print("Word\tTimes\tAverage times per Sentences")
print("----\t-----------\t----------------------")
for a,b in counts.take(30):
    print("{}\t{}\t\t\t{:.2f}".format(a, b , float(a)/float(total)))

counts.saveAsTextFile("/hw3/output/out01")


# In[13]:


# check answer in hadoop 
get_ipython().system('hadoop fs -cat /hw3/output/out01/part-00000 | head -30')


# In[14]:


get_ipython().system('hdfs dfs -ls /hw3/output/')


# In[15]:


get_ipython().system('hdfs dfs -rm -r /hw3/output/out01')


# In[ ]:




