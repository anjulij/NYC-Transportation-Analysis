#include <iostream>
#include <vector>
#include <math>

// struct for the each of the points
struct Point {
    
    // cords of the point
    double x;
    double y;

    Point(): x(0.0), y(0.0) {};
    ~Point() {};
};

// PSUEDO CODE GIVEN FROM WIKIPEDIA
/*
def k_means_cluster(k, points):
    # Initialization: choose k centroids (Forgy, Random Partition, etc.)
    centroids = [c1, c2, ..., ck]
    
    # Initialize clusters list
    clusters = [[] for _ in range(k)]
    
    # Loop until convergence
    converged = false
    while not converged:
        # Clear previous clusters
        clusters = [[] for _ in range(k)]
    
        # Assign each point to the "closest" centroid 
        for point in points:
            distances_to_each_centroid = [distance(point, centroid) for centroid in centroids]
            cluster_assignment = argmin(distances_to_each_centroid)
            clusters[cluster_assignment].append(point)
        
        # Calculate new centroids
        #   (the standard implementation uses the mean of all points in a
        #     cluster to determine the new centroid)
        new_centroids = [calculate_centroid(cluster) for cluster in clusters]
        
        converged = (new_centroids == centroids)
        centroids = new_centroids
        
        if converged:
            return clusters
*/

// Determine the distance between two clusters
double dist(double x, double y) {
    double res;
    res = pow(x - y, 2);
    return sqrt(res)
}

// I am assuming the data will be stored in a 2d array, if not this can be changed quite easily
// k will represent the number of clusters
void k_means_cluster(const vector<vector<double>>& data, int k, vector<int> centroids) {

}