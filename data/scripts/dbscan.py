import calendar
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
        
        # find k neighbors of point xi 
        distances, indices = tree.query(X.iloc[xi:xi+1,:], k=minSamples)

        # check if datapoint is noise (k neighbors not within epsilon distance)
        if( not all(d < eps for d in distances[0])):
            labels[xi] = -1

        # otherwise create a new cluster with center xi  
        else: 
           c += 1
           labels[xi] = c
           expandCluster(X, tree, labels, indices[0], c, eps, minSamples)
    
    end_time_dbscan = time.time()
    elapsed_time_dbscan = end_time_dbscan - start_time_dbscan
    print(f"DBSCAN completed in {elapsed_time_dbscan:.2f} seconds.")
    
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
            distances, indices = tree.query(X.iloc[xn:xn+1,:], k=minSamples)
            
            # Check if borderpoints should be added to list of neighbors
            if all(d < eps for d in distances[0]):
                neighbors=np.append(neighbors, indices[0])
            
        i += 1        

# Fetch data from PostgreSQL and extract day and hour from timestamp
print(f"Fetching data")
start_time = time.time()

# Define the specific time frame (e.g., Monday between 8 AM and 10 AM)
desired_day = 0
start_hour = 8
end_hour = 10

sbwy = fetch_data_from_db(None, desired_day=desired_day, start_hour=start_hour, end_hour=end_hour)

if sbwy is None or sbwy.empty:
    raise ValueError("Filtered data is empty. Please verify the query parameters.")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Fetch completed in {elapsed_time:.2f} seconds.")

print("Parsing data")
try:
    sbwy['transit_timestamp'] = pd.to_datetime(sbwy['transit_timestamp'])
    sbwy['day'] = sbwy['transit_timestamp'].dt.weekday
    sbwy['hour'] = sbwy['transit_timestamp'].dt.hour
except Exception as e:
    raise ValueError(f"Error parsing data: {e}")

#set hyperparameters 
eps = 0.3
minSamples = 5

# apply dbscan
print(f"Applying DBSCAN to data from day {desired_day} between {start_hour}:00 and {end_hour}:00")
sbwy.loc[:, 'cluster'] = dbscan(sbwy[['latitude', 'longitude', 'ridership', 'hour']], eps=0.3, minSamples=5)

print(f"Plotting results")
# plot results
day_name = calendar.day_name[desired_day]
fig = px.scatter_mapbox(
    sbwy, lat='latitude', 
    lon='longitude', 
    color='cluster', 
    size='ridership', 
    color_continuous_scale=px.colors.sequential.Blackbody, 
    size_max=15, zoom=10,
    mapbox_style="carto-positron", 
    title=f'DBSCAN Clustering Results {day_name}, {start_hour}:00 - {end_hour}:00')

fig.show()
fig.write_html(f"../../website/src/assets/generated_plots/dbscan_{day_name}.html")

print(f"Plot saved to dbscan_{day_name}.html")