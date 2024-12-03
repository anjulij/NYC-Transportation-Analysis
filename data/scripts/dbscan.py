import time
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.neighbors import KDTree

from query_data import fetch_data_from_db

# dbscan function retuns a list of cluster labels, with -1 being the value for noise
def dbscan(Xoriginal, eps, minSamples):
    # Normalizing the data
    X=(Xoriginal-Xoriginal.min())/(Xoriginal.max()-Xoriginal.min())

    #Create KD tree datastructure
    tree=KDTree(X,leaf_size=15)

    # initialize labels   
    labels = [0]*len(X)

    # initialize cluster number
    c = 0

    # Total number of points
    total_points = len(X)

    print(f"Total points: {total_points}")

    start_time_dbscan = time.time()
    # iterate through datapoints to find new center
    for xi in range(0, len(X)):
        # Print progress percentage
        progress = (xi + 1) / total_points * 100
        print(f"Progress: {progress:.2f}%", end='\r')

        # check if point xi has already been assigned to a cluster
        if not (labels[xi] == 0):
           continue
        
        # find neighbors within distance epsilon of xi 
        indices = tree.query_radius(X.iloc[xi:xi+1,:], r=eps)  

        # check if datapoint is noise (not enough neighbors)
        if( len(indices[0]) < minSamples):
            labels[xi] = -1

        # otherwise create a new cluster with center xi  
        else: 
           c += 1
           labels[xi] = c
           expandCluster(X, tree, labels, indices[0], c, eps, minSamples)
    
    end_time_dbscan = time.time()
    elapsed_time_dbscan = end_time_dbscan - start_time_dbscan
    print(f"Fetch completed in {elapsed_time_dbscan:.2f} seconds.")
    
    return labels

#looks for all the datapoints belonging to a new cluster
def expandCluster(X, tree, labels, neighbors, c, eps, minSamples):
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
            indices = tree.query_radius(X.iloc[xn:xn+1,:], r=eps) 
            
            # Check if borderpoints should be added to list of neighbors
            if (len(indices[0]) >= minSamples):
                neighbors=np.append(neighbors, indices[0])
            
        i += 1        

# Fetch data from PostgreSQL and extract day and hour from timestamp
print(f"Fetching data")
start_time = time.time()

sbwy = fetch_data_from_db() 
# sbwy = pd.read_csv('C:/Users/Soto/Documents/GitHub/NYC-Transportation-Analysis/data/samples/mta_subway_sample.csv')

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Fetch completed in {elapsed_time:.2f} seconds.")

print(f"Parsing data")
sbwy['transit_timestamp']= pd.to_datetime(sbwy['transit_timestamp'])
sbwy['day']= sbwy['transit_timestamp'].dt.weekday
sbwy['hour']= sbwy['transit_timestamp'].dt.hour
sbwy.head()

#set hyperparameters 
eps = 0.3
minSamples = 5

print(f"Applying DBSCAN")
# apply dbscan
sbwy['cluster'] = dbscan(sbwy[['latitude','longitude','ridership','hour']], eps, minSamples)

print(f"Plotting results")
# plot results
fig = px.scatter_mapbox(sbwy, lat='latitude', lon='longitude', color='cluster', size='ridership', color_continuous_scale=px.colors.sequential.Blackbody, size_max=15, zoom=10,
                        mapbox_style="carto-positron", title='DBSCAN Clustering Results')
fig.show()