import calendar
import random
import time
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.metrics.pairwise import euclidean_distances
from query_data import fetch_data_from_db

def calc_centroid(cluster_data):
    
    return cluster_data.mean(axis=0)

def k_means(points, k, max_iter=100):

    # Randomly initialize centroids
    centroids = points.sample(n=k).to_numpy()
    clusters = [0] * len(points)

    converged = False
    iteration = 0

    total_points = len(points)
    print(f"Total points: {total_points}")
    start_time = time.time()

    while not converged and iteration < max_iter:
        iteration += 1

        # Compute distances to centroids and assign clusters
        distances = euclidean_distances(points, centroids)
        new_clusters = np.argmin(distances, axis=1)

        # Check for convergence
        if np.array_equal(clusters, new_clusters):
            converged = True
        clusters = new_clusters

        # Update centroids
        for i in range(k):
            cluster_points = points[clusters == i]
            if len(cluster_points) > 0:
                centroids[i] = cluster_points.mean(axis=0)

    end_time = time.time()
    print(f"K-means completed in {end_time - start_time:.2f} seconds and {iteration} iterations.")
    return clusters, centroids

# Fetch data from PostgreSQL
print("Fetching data")
start_time = time.time()
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

# Prepare data for clustering
data = sbwy[['latitude', 'longitude', 'ridership']].dropna()

# Set hyperparameters
k = 5
print(f"Applying K-means to data from day {desired_day} between {start_hour}:00 and {end_hour}:00")
clusters, centroids = k_means(data, k)

# Add cluster labels to data
sbwy.loc[data.index, 'cluster'] = clusters

# Create a DataFrame for centroids
centroids_df = pd.DataFrame(centroids, columns=['latitude', 'longitude', 'ridership'])

# Plot results
day_name = calendar.day_name[desired_day]
fig = px.scatter_mapbox(
    sbwy, 
    lat='latitude', 
    lon='longitude', 
    color='cluster', 
    size='ridership', 
    color_continuous_scale=px.colors.sequential.Magma, 
    size_max=15, 
    zoom=10,
    mapbox_style='carto-darkmatter',     
    title=f'K-means Clustering Results {day_name}, {start_hour}:00 - {end_hour}:00'
)

# Add centroids to the map
fig.add_scattermapbox(
    lat=centroids_df['latitude'],
    lon=centroids_df['longitude'],
    mode='markers',
    marker=dict(size=15, color='black', symbol='x'),
    name='Centroids'
)

# Set transparent backgrounds and white font for dark mode
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)', 
    font=dict(color='#ffffff'),  
    title_font=dict(color='#ffffff'),
    # Border
    shapes=[
        dict(
            type="rect",
            x0=0, y0=0, x1=1, y1=1,
            xref="paper", yref="paper",
            line=dict(color="white", width=3)
        )
    ]
)

fig.show()
fig.write_html(f"../../website/src/assets/generated_plots/kmeans_{day_name}.html")

print(f"Plot saved to kmeans_{day_name}.html")