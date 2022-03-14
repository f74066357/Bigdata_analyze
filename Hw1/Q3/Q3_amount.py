# print(temp.columns)
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

taxiDB=pd.concat([taxiDB1,taxiDB2,taxiDB3],axis=0)


amount = np.array(list(taxiDB['Total_Amt']))
Limits = [np.percentile(amount, 1), np.percentile(amount, 99)]
print(Limits) #[3.3, 49.15]
taxiDB = taxiDB[(taxiDB['Total_Amt']   >= Limits[0] ) & (taxiDB['Total_Amt']   <= Limits[1]) ]
L50,L70,L90 = np.percentile(amount, 50),np.percentile(amount, 70),np.percentile(amount, 90)
print(L50,L70,L90)

# sns.distplot(amount)
plt.hist(amount)
plt.vlines(L50,0,0.2,color="green")
plt.vlines(L70,0,0.2,color="blue")
plt.xlabel('Amounts')
plt.ylabel('')
plt.show()

taxiDBs = taxiDB[(taxiDB['Total_Amt']   < 10.7)]
taxiDBs = taxiDBs.reset_index(drop=True)
taxiDBb = taxiDB[(taxiDB['Total_Amt']   >= 10.7)]
taxiDBb = taxiDBb.reset_index(drop=True)

#time
formate = '%Y-%m-%d %H:%M:%S'
bi = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24]
def time_obj(dfrow):
    return time.strptime(dfrow, formate).tm_hour

pick_hs = list(map(time_obj, taxiDBs['Trip_Pickup_DateTime']))
plt.hist(pick_hs, bins=bi)
plt.xlabel('HR_pick_small')
plt.ylabel('Counts')
plt.show()
drop_hs = list(map(time_obj, taxiDBs['Trip_Dropoff_DateTime']))
plt.hist(drop_hs, bins=bi)
plt.xlabel('HR_drop_small')
plt.ylabel('Counts')
plt.show()

pick_hb = list(map(time_obj, taxiDBb['Trip_Pickup_DateTime']))
plt.hist(pick_hb, bins=bi)
plt.xlabel('HR_pick_big')
plt.ylabel('Counts')
plt.show()
drop_hb = list(map(time_obj, taxiDBb['Trip_Dropoff_DateTime']))
plt.hist(drop_hb, bins=bi)
plt.xlabel('HR_drop_big')
plt.ylabel('Counts')
plt.show()


# Payment_Type
taxiDBs['Payment_Type'] = taxiDBs['Payment_Type'].str.upper()
taxiDBb['Payment_Type'] = taxiDBb['Payment_Type'].str.upper()

def paytype(s):
    if(s=="CASH"):
        return 0
    elif(s=="CREDIT"):
        return 1
    else:
        return 2
bi= ["CASH","CREDIT","OTHERS"]

# pays = list(map(paytype, taxiDBs['Payment_Type']))
# payb = list(map(paytype, taxiDBb['Payment_Type']))
pays = list(taxiDBs['Payment_Type'])
payb = list(taxiDBb['Payment_Type'])

pd.Series(pays).value_counts().plot(kind='bar')
plt.show()
pd.Series(payb).value_counts().plot(kind='bar')
plt.show()



# Trip_Distance
dists = list(taxiDBs['Trip_Distance'])
distb = list(taxiDBb['Trip_Distance'])
print(distb[:10])

sns.distplot(dists)
plt.xlabel('Trip_Distance Small')
plt.ylabel('Counts')
plt.show()

sns.distplot(distb)
plt.xlabel('Trip_Distance Big')
plt.ylabel('Counts')
plt.show()

