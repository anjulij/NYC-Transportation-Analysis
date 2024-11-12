import numpy as np
import pandas as pd
import plotly.express as px

# dbscan function retuns a list of cluster labels, with -1 being the value for noise
def dbscan(X, epsilon, minSamples):
    # initialize labels   
    labels = [0]*len(X)

    # initialize cluster number
    c = 0
    
    # iterate through datapoints to find new center
    for xi in range(0, len(X)):
    
        if not (labels[xi] == 0):
           continue
        
        # find all neighbor points
        NeighborPts = region_query(X, xi, epsilon)
        
        # check if datapoint is noise
        if len(NeighborPts) < minSamples:
            labels[xi] = -1
           
        else: 
           c += 1
           grow_cluster(X, labels, xi, NeighborPts, c, epsilon, minSamples)
    
    return labels

#looks for all the datapoints belonging to a new cluster
def grow_cluster(X, labels, xi, NeighborPts, c, epsilon, minSamples):
    
    labels[xi] = c
    i = 0
    while i < len(NeighborPts):    
        
        # Get the next point from the queue.        
        xn = NeighborPts[i]
       
        # Relable noise datapoints
        if labels[xn] == -1:
           labels[xn] = c
        
        elif labels[xn] == 0:
            labels[xn] = c
            # Find neighbors of xn
            xnNeighborPts = region_query(X, xn, epsilon)
            
            # Check if branch datapoint
            if len(xnNeighborPts) >= minSamples:
                NeighborPts = NeighborPts + xnNeighborPts
        i += 1        

# Find points that are within epsilon distance
def region_query(X, xi, epsilon):
    neighbors = []
    
    for xn in range(0, len(X)):
        if np.linalg.norm(X.loc[xi] - X.loc[xn]) < epsilon:
           neighbors.append(xn)

    return neighbors

# read dataset and extract day and hour from timestamp
sbwy = pd.read_csv("data/samples/mta_subway_sample.csv", usecols=[0, 7, 9, 10], header=0)
sbwy['transit_timestamp']= pd.to_datetime(sbwy['transit_timestamp'])
sbwy['day']= sbwy['transit_timestamp'].dt.weekday
sbwy['hour']= sbwy['transit_timestamp'].dt.hour
sbwy.head()

#set hyperparameters
epsilon = 0.1
minSamples = 10

# apply dbscan
sbwy['cluster'] = dbscan(sbwy[['latitude','longitude','ridership','day','hour']], epsilon, minSamples)

# plot results
fig = px.scatter(sbwy, x='latitude', y='longitude', color='cluster', 
                 title='DBSCAN Clustering Results')
fig.show()