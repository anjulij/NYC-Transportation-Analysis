#include <iostream>
#include <vector>
#include <cmath>
#include <time.h>

// struct for the each of the points
struct Point {
    
    // cords of the point
    // for now, I am using the distance of each rider to calculate k-means, but we can easily change this to something else
    double x;
    double y;
    
    // These two variables come from mta_subway_sample.csv
    int station_complex_id; // Used to determine which station we are looking at
    int ridership;          // Number of riders at that station

    Point(double x_inp, double y_inp, int id, int riders) : x(x_inp), y(y_inp), station_complex_id(id), ridership(riders) {};
};

// Used to calculate the centroid of a specific cluster
Point calcCentroid(const std::vector<Point>& cluster, int id) {
    double sumx = 0.0;
    double sumy = 0.0;
    int riders;
    for (const Point p : cluster) { // Take each point in the cluster and add up their x, y positions and the number of riders
        sumx += p.x;
        sumy += p.y;
        riders += p.ridership;
    }
    // Take the sums and divide by the total number of points
    return Point(sumx / cluster.size(), sumy / cluster.size(), riders / cluster.size(), id);

}

// Determine the distance between two points
double dist(const Point& point1, const Point& point2) {

    double pos_res, rider_res;
    pos_res = pow(point1.x - point2.x, 2) + (point1.y - point2.y, 2);
    pos_res = sqrt(pos_res);

    rider_res = pow(point1.ridership - point2.ridership, 2);
    rider_res = sqrt(rider_res);

    return sqrt(pow(pos_res, 2) + pow(rider_res, 2));
}

// k will represent the number of clusters
void k_means_cluster(const std::vector<Point>& points, int k) {
    
    // Randomly choose initital centroids k
    // used the example from the cplusplus.com rand function page
    srand(time(NULL));              // initialize random seed
    int random = rand() % k;   // This will choose a number between 1 and k

    // Initialize a vector of points containing points from the begining of the centroid to random
    std::vector<Point> centroids(points.begin(), points.begin() + random);
}
