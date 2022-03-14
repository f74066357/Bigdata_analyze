import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import time
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier

taxiDB1 = pd.read_csv('yellow_tripdata_2009-01.csv')
taxiDB2 = pd.read_csv('yellow_tripdata_2009-02.csv')
taxiDB3 = pd.read_csv('yellow_tripdata_2009-03.csv')

formate = '%Y-%m-%d %H:%M:%S'
bi = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24]
def time_obj(dfrow):
    return time.strptime(dfrow, formate).tm_hour
pick_h = list(map(time_obj, taxiDB1['Trip_Pickup_DateTime']))+list(map(time_obj, taxiDB2['Trip_Pickup_DateTime']))+list(map(time_obj, taxiDB3['Trip_Pickup_DateTime']))
drop_h = list(map(time_obj, taxiDB1['Trip_Dropoff_DateTime']))+list(map(time_obj, taxiDB2['Trip_Dropoff_DateTime']))+list(map(time_obj, taxiDB3['Trip_Dropoff_DateTime']))


# sns.distplot(pick_h)
# plt.xlabel('HR_pick')
# plt.ylabel('Counts')
# plt.show()
# plt.close()
'''
plt.hist(pick_h, bins=bi)
plt.xlabel('HR_pick')
plt.ylabel('Counts')
plt.show()
'''
# sns.distplot(drop_h)
# plt.xlabel('HR_pick')
# plt.ylabel('Counts')
# plt.show()
# plt.close()

plt.hist(drop_h, bins=bi)
plt.xlabel('HR_drop')
plt.ylabel('Counts')
plt.show()
