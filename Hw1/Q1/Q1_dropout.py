import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier

matplotlib.style.use('fivethirtyeight')
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['figure.figsize'] = (10,10)

taxiDB1 = pd.read_csv('yellow_tripdata_2009-01.csv')
taxiDB2 = pd.read_csv('yellow_tripdata_2009-02.csv')
taxiDB3 = pd.read_csv('yellow_tripdata_2009-03.csv')

allLat  = np.array(list(taxiDB1['End_Lat'])+ list(taxiDB2['End_Lat'])+ list(taxiDB3['End_Lat']))
allLong = np.array(list(taxiDB1['End_Lon'])+ list(taxiDB2['End_Lon'])+ list(taxiDB3['End_Lon']))

longLimits = [np.percentile(allLong, 2.5), np.percentile(allLong, 97.5)]
latLimits  = [np.percentile(allLat , 2.5), np.percentile(allLat , 97.5)]

print(str(longLimits)+" "+str(latLimits))

taxiDB1 = taxiDB1[(taxiDB1['End_Lat']   >= latLimits[0] ) & (taxiDB1['End_Lat']   <= latLimits[1]) ]
taxiDB1 = taxiDB1[(taxiDB1['End_Lon']  >= longLimits[0]) & (taxiDB1['End_Lon']  <= longLimits[1])]
taxiDB1 = taxiDB1.reset_index(drop=True)

taxiDB2 = taxiDB2[(taxiDB2['End_Lat']   >= latLimits[0] ) & (taxiDB2['End_Lat']   <= latLimits[1]) ]
taxiDB2 = taxiDB2[(taxiDB2['End_Lon']  >= longLimits[0]) & (taxiDB2['End_Lon']  <= longLimits[1])]
taxiDB2 = taxiDB2.reset_index(drop=True)

taxiDB3 = taxiDB3[(taxiDB3['End_Lat']   >= latLimits[0] ) & (taxiDB3['End_Lat']   <= latLimits[1]) ]
taxiDB3 = taxiDB3[(taxiDB3['End_Lon']  >= longLimits[0]) & (taxiDB3['End_Lon']  <= longLimits[1])]
taxiDB3 = taxiDB3.reset_index(drop=True)

allLat  = np.array(list(taxiDB1['End_Lat'])+ list(taxiDB2['End_Lat'])+ list(taxiDB3['End_Lat']))
allLong = np.array(list(taxiDB1['End_Lon'])+ list(taxiDB2['End_Lon'])+ list(taxiDB3['End_Lon']))


#####
plt.figure(figsize = (10,10))
plt.plot(allLong,allLat,'.', alpha = 0.4, markersize = 0.05)
plt.savefig("Plot rides_Dropout")

loc_df = pd.DataFrame()
loc_df['longitude'] = allLong
loc_df['latitude'] = allLat

kmeans = KMeans(n_clusters=10).fit(loc_df)
loc_df['label'] = kmeans.labels_

#loc_df = loc_df.sample(200000)
plt.figure(figsize = (10,10))
for label in loc_df.label.unique():
    plt.plot(loc_df.longitude[loc_df.label == label],loc_df.latitude[loc_df.label == label],'.', alpha = 0.3, markersize = 0.3)

plt.title('Clusters of New York_Dropout')
plt.savefig("Clusters of New York_Dropout")

###
fig,ax = plt.subplots(figsize = (10,10))
for label in loc_df.label.unique():
    ax.plot(loc_df.longitude[loc_df.label == label],loc_df.latitude[loc_df.label == label],'.', alpha = 0.3, markersize = 0.3)
    ax.plot(kmeans.cluster_centers_[label,0],kmeans.cluster_centers_[label,1],'o', color = 'r')
    ax.annotate(label, (kmeans.cluster_centers_[label,0],kmeans.cluster_centers_[label,1]), color = 'b', fontsize = 20)
ax.set_title('Cluster Centers_Dropout')
plt.savefig("Cluster Centers_Dropout")

####
print(loc_df['label'].value_counts())