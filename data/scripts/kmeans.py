import random
import math
import csv
import plotly.express as px
import plotly.graph_objects as go
from query_data import fetch_data_from_db

class Point:
    def __init__(self, x, y, ridership):
        self.x = x
        self.y = y
        self.ridership = ridership

def calc_centroid(cluster):
    sum_x = sum(point.x for point in cluster)
    sum_y = sum(point.y for point in cluster)
    sum_riders = sum(point.ridership for point in cluster)
    return Point(sum_x / len(cluster), sum_y / len(cluster), sum_riders / len(cluster))

def dist(point1, point2):
    pos_res = (point1.x - point2.x)**2 + (point1.y - point2.y)**2
    return math.sqrt(pos_res)

def k_means_cluster(points, k):
    random.seed()
    centroids = random.sample(points, k)
    clusters = [0] * len(points)

    converged = False
    while not converged:
        converged = True
        
        for i, point in enumerate(points):
            distances = [dist(point, centroid) for centroid in centroids]
            nearest_centroid = distances.index(min(distances))
            if clusters[i] != nearest_centroid:
                clusters[i] = nearest_centroid
                converged = False

        for i in range(k):
            cluster_points = [point for j, point in enumerate(points) if clusters[j] == i]
            if cluster_points:
                centroids[i] = calc_centroid(cluster_points)

    return centroids, clusters

def generate_colors(total):
    return px.colors.qualitative.Plotly[:total]

def main():
    # Define the specific time frame (e.g., Monday between 8 AM and 10 AM)
    desired_day = 1
    start_hour = 8
    end_hour = 10
    fetch_data_from_db(output_csv="mta_subway.csv", desired_day=desired_day, start_hour=start_hour, end_hour=end_hour)
    with open('mta_subway.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        
        points = []
        for row in reader:
            try:
                ridership = int(row[7])
                lat = float(row[9])
                lon = float(row[10])
                points.append(Point(lat, lon, ridership))
            except (ValueError, IndexError):
                continue

    k = int(input("Enter the number of clusters: "))
    centroids, clusters = k_means_cluster(points, k)

    cluster_x = [[] for _ in range(k)]
    cluster_y = [[] for _ in range(k)]
    riders = [[] for _ in range(k)]
    
    fig = go.Figure()

    colors = generate_colors(k)
    for i in range(k):
        fig.add_trace(go.Scatter(
            x=cluster_x[i],
            y=cluster_y[i],
            mode='markers',
            marker=dict(size=riders[i], color=colors[i]),
            name=f"Cluster {i}"
        ))

    x_centroids = [centroid.x for centroid in centroids]
    y_centroids = [centroid.y for centroid in centroids]
    fig.add_trace(go.Scatter(
        x=x_centroids,
        y=y_centroids,
        mode='markers',
        marker=dict(size=15, color='black', symbol='x'),
        name="Centroids"
    ))

    fig.update_layout(
        title="K-means Clustering based on Distance and Ridership",
        xaxis_title="Longitude",
        yaxis_title="Latitude",
        legend_title="Clusters"
    )

    fig.show()

if __name__ == "__main__":
    main()