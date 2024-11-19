import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.cluster import DBSCAN
from sklearn import preprocessing

# dbscan function retuns a list of cluster labels, with -1 being the value for noise
def dbscan(Xoriginal, eps, minSamples):
    # Normalizing the data
    X=(Xoriginal-Xoriginal.min())/(Xoriginal.max()-Xoriginal.min())
    print(X)

    # initialize labels   
    labels = [0]*len(X)

    # initialize cluster number
    c = 0
    
    # iterate through datapoints to find new center
    for xi in range(0, len(X)):

        # check if point xi has already been assigned to a cluster
        if not (labels[xi] == 0):
           continue
        
        # find all neighbors of point xi
        neighbors = findNeighbors(X, xi, eps)
        
        # check if datapoint is noise (doesn't have enough neighbors)
        if len(neighbors) < minSamples:
            labels[xi] = -1

        # otherwise create a new cluster with center xi  
        else: 
           c += 1
           labels[xi] = c
           expandCluster(X, labels, neighbors, c, eps, minSamples)
    
    return labels

#looks for all the datapoints belonging to a new cluster
def expandCluster(X, labels, neighbors, c, eps, minSamples):
    
    i = 0
    while i < len(neighbors):    
        
        # get next neighbor xn       
        xn = neighbors[i]
       
        # check if xn was previously labeled as noise and relabel if needed
        if labels[xn] == -1:
           labels[xn] = c
        
        #check if xn is unassigned to a cluster and create new label if needed
        elif labels[xn] == 0:
            labels[xn] = c
            # Find neighbors of xn
            borderPoints= findNeighbors(X, xn, eps)
            
            # Check if borderpoints should be added to list of neighbors
            if len(borderPoints) >= minSamples:
                neighbors = neighbors + borderPoints
        i += 1        

# Find points that are within eps distance
def findNeighbors(X, xi, eps):
    neighbors = []
    
    # check if 2-norm is less than eps
    for xn in range(0, len(X)):
        if np.linalg.norm(X.loc[xi] - X.loc[xn]) < eps:
           neighbors.append(xn)

    return neighbors

# read dataset and extract day and hour from timestamp
sbwy = pd.read_csv("data/samples/mta_subway_sample.csv", usecols=[0, 7, 9, 10], header=0)
sbwy['transit_timestamp']= pd.to_datetime(sbwy['transit_timestamp'])
sbwy['day']= sbwy['transit_timestamp'].dt.weekday
sbwy['hour']= sbwy['transit_timestamp'].dt.hour
sbwy.head()

#set hyperparameters 
eps = 0.3
minSamples = 5

# apply dbscan
sbwy['cluster'] = dbscan(sbwy[['latitude','longitude','ridership','hour']], eps, minSamples)

# plot results
fig = px.scatter_mapbox(sbwy, lat='latitude', lon='longitude', color='cluster', size='ridership', color_continuous_scale=px.colors.sequential.Blackbody, size_max=15, zoom=10,
                        mapbox_style="carto-positron", title='DBSCAN Clustering Results')
fig.show()

# comparing with Scikit library
scaler=preprocessing.MinMaxScaler()
clustering = DBSCAN(eps=eps, min_samples=minSamples).fit(scaler.fit_transform(sbwy[['latitude','longitude','ridership','hour']]))
sbwy['cluster_sklearn']=clustering.labels_
fig2 = px.scatter_mapbox(sbwy, lat='latitude', lon='longitude', color='cluster_sklearn', size='ridership', color_continuous_scale=px.colors.sequential.Blackbody, size_max=15, zoom=10,
                        mapbox_style="carto-positron", title='Sklearn Clustering Results')
fig2.show()