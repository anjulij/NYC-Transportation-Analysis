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
    
    // Not sure if this will be used in final iteration of K-means function
    //int station_complex_id; // Used to determine which station we are looking at

    int ridership;          // Number of riders at that station

    Point(double x_inp, double y_inp, int riders) : x(x_inp), y(y_inp), ridership(riders) {};
};

// Used to calculate the centroid of a specific cluster
Point calcCentroid(const std::vector<Point>& cluster) {

    double sumx = 0.0;
    double sumy = 0.0;
    int riders;
    for (const Point p : cluster) { // Take each point in the cluster and add up their x, y positions and the number of riders
        sumx += p.x;
        sumy += p.y;
        riders += p.ridership;
    }
    // Take the sums and divide by the total number of points
    return Point(sumx / cluster.size(), sumy / cluster.size(), riders / cluster.size());

}

// Determine the distance between two points
double dist(const Point& point1, const Point& point2) {

    double pos_res, rider_res;
    pos_res = pow(point1.x - point2.x, 2) + (point1.y - point2.y, 2);

    rider_res = pow(point1.ridership - point2.ridership, 2);

    return sqrt(pos_res + rider_res);
}

// A lot of "Inspiration" came from the K-means wikipedia article, psuedo-code and more technical aspects explained there made this
// much easier to impliment.

// k will represent the number of clusters
void k_means_cluster(const std::vector<Point>& points, int k) {
    
    // Randomly choose initital centroids k
    // used the example from the cplusplus.com rand function page
    srand(time(NULL));              // initialize random seed

    // Initialize a vector of centroids
    std::vector<Point> centroids;

    for (int i = 0; i < k; ++i) {
        int random = rand() % points.size(); // Choose a centroid at random
        centroids.push_back(points[random]);
    }
    // Vector that will track the points and their respective clusters
    std::vector<int> clusters(points.size());

    // Loop until no points change cluster
    bool converged = false;
    while(!converged) {

        for (int i = 0; i < points.size(); ++i) {
            int near_cent;
            double minimum;

            // Assign each point to the "closest" centroid
            for (int j = 0; j < centroids.size(); ++j) {

                double distance = dist(points[i], centroids[j]);

                // If there is another closer centroid
                if(distance < minimum) {
                    minimum = distance; // new closest
                    near_cent = j;      // new closest centroid
                }
            }

            // If a point was assigned to a cluster that was not previously assigned to it, store it and converged is still true
            if(clusters[i] != near_cent) {
                clusters[i] = near_cent;
                converged = true;
            }
        }
        // Calculate new centroids
        // (the standard implementation uses the mean of all points in a
        // cluster to determine the new centroid)

        for (int i = 0; i < centroids.size(); ++i) {

            std::vector<Point> c_Points;    // cluster containing the points
            for (int j = 0; j < points.size(); ++j) {   // the points within the cluser
                if(clusters[j] == i) {  // Check if point "i" is in cluster "j"
                    c_Points.push_back(points[i]); // push point "i" into the cluster
                }
            }
            centroids[i] = calcCentroid(c_Points);
        }
    }
}

int main() {

    /*
    TODO: Update main to read from test data and verify k-means accuracy
    */
    return 0;
}
