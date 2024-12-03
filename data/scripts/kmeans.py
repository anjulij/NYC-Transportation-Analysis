import random
import math
import matplotlib.pyplot as plt
import csv

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
    base_colors = ["#FF0000", "#00FF00", "#0000FF", "#00FFFF", "#FF00FF", "#808080", "#808000", "#800080", "#008080", "#000080"]
    while len(base_colors) < total:
        base_colors.append(f"#{random.randint(0, 0xFFFFFF):06x}")
    return base_colors

def main():
    with open('../data/samples/mta_subway_sample.csv', 'r') as file:
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
    
    for i, point in enumerate(points):
        cluster_x[clusters[i]].append(point.x)
        cluster_y[clusters[i]].append(point.y)
        riders[clusters[i]].append(point.ridership)

    x_centroids = [centroid.x for centroid in centroids]
    y_centroids = [centroid.y for centroid in centroids]
    colors = generate_colors(k)

    for i in range(k):
        plt.scatter(cluster_x[i], cluster_y[i], s=riders[i], color=colors[i], label=f"Cluster {i}")

    plt.scatter(x_centroids, y_centroids, s=200, color="black", marker="x", label="Centroids")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("K-means clustering based on distance and ridership")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
