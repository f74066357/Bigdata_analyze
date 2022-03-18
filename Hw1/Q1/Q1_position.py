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

taxiDB=pd.concat([taxiDB1,taxiDB2,taxiDB3],axis=0)

allLat  = np.array(list(taxiDB['Start_Lat'])  + list(taxiDB['End_Lat']))
allLong = np.array(list(taxiDB['Start_Lon']) + list(taxiDB['End_Lon']))

longLimits = [np.percentile(allLong, 3), np.percentile(allLong, 97)]
latLimits  = [np.percentile(allLat , 3), np.percentile(allLat , 97)]

taxiDB = taxiDB[(taxiDB['Start_Lat']   >= latLimits[0] ) & (taxiDB['Start_Lat']   <= latLimits[1]) ]
taxiDB = taxiDB[(taxiDB['End_Lat']  >= latLimits[0] ) & (taxiDB['End_Lat']  <= latLimits[1]) ]
taxiDB = taxiDB[(taxiDB['Start_Lon']  >= longLimits[0]) & (taxiDB['Start_Lon']  <= longLimits[1])]
taxiDB = taxiDB[(taxiDB['End_Lon'] >= longLimits[0]) & (taxiDB['End_Lon'] <= longLimits[1])]
taxiDB = taxiDB.reset_index(drop=True)

allLat  = np.array(list(taxiDB['Start_Lat'])  + list(taxiDB['End_Lat']))
allLong = np.array(list(taxiDB['Start_Lon']) + list(taxiDB['End_Lon']))

'''
# convert fields to sensible units
medianLat  = np.percentile(allLat,50)
medianLong = np.percentile(allLong,50)

latMultiplier  = 111.32
longMultiplier = np.cos(medianLat*(np.pi/180.0)) * 111.32

taxiDB['src lat [km]']   = latMultiplier  * (taxiDB['Start_Lat']   - medianLat)
taxiDB['src long [km]']  = longMultiplier * (taxiDB['Start_Lon']  - medianLong)
taxiDB['dst lat [km]']   = latMultiplier  * (taxiDB['End_Lat']  - medianLat)
taxiDB['dst long [km]']  = longMultiplier * (taxiDB['End_Lon'] - medianLong)

allLat  = np.array(list(taxiDB['src lat [km]'])  + list(taxiDB['dst lat [km]']))
allLong = np.array(list(taxiDB['src long [km]']) + list(taxiDB['dst long [km]']))

fig, axArray = plt.subplots(nrows=1,ncols=2)
axArray[0].hist(allLat ,80); axArray[0].set_xlabel('latitude [km]')
axArray[1].hist(allLong,80); axArray[1].set_xlabel('longitude [km]')
plt.savefig("histograms of latitude and longitude")
'''
#####

plt.figure(figsize = (10,10))
plt.plot(allLong,allLat,'.', alpha = 0.4, markersize = 0.05)
plt.savefig("Plot rides")

loc_df = pd.DataFrame()
loc_df['longitude'] = allLong
loc_df['latitude'] = allLat

kmeans = KMeans(n_clusters=5).fit(loc_df)
loc_df['label'] = kmeans.labels_

plt.figure(figsize = (10,10))
for label in loc_df.label.unique():
    plt.plot(loc_df.longitude[loc_df.label == label],loc_df.latitude[loc_df.label == label],'.', alpha = 0.3, markersize = 0.3)

plt.title('Clusters of New York')
plt.savefig("Clusters of New York")

###
fig,ax = plt.subplots(figsize = (10,10))
for label in loc_df.label.unique():
    ax.plot(loc_df.longitude[loc_df.label == label],loc_df.latitude[loc_df.label == label],'.', alpha = 0.3, markersize = 0.3)
    ax.plot(kmeans.cluster_centers_[label,0],kmeans.cluster_centers_[label,1],'o', color = 'r')
    ax.annotate(label, (kmeans.cluster_centers_[label,0],kmeans.cluster_centers_[label,1]), color = 'b', fontsize = 20)
ax.set_title('Cluster Centers')
plt.savefig("Cluster Centers")
####
'''
imageSize = (700,700)
longRange = [-5,12]
latRange = [-10,8]

allLatInds  = imageSize[0] - (imageSize[0] * (allLat  - latRange[0])  / (latRange[1]  - latRange[0]) ).astype(int)
allLongInds = (imageSize[1] * (allLong - longRange[0]) / (longRange[1] - longRange[0])).astype(int)

locationDensityImage = np.zeros(imageSize)
for latInd, longInd in zip(allLatInds,allLongInds):
    locationDensityImage[latInd,longInd] += 1

fig, ax = plt.subplots(nrows=1,ncols=1)
ax.imshow(np.log(locationDensityImage+1),cmap='hot')
ax.set_axis_off()
plt.savefig("spatial density plot of the pickup and dropoff locations")

'''
print(loc_df['label'].value_counts())
