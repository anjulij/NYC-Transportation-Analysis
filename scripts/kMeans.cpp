#include <iostream>
#include <stdio.h>
#include <string.h>
#include <iomanip>
#include <string>
#include <vector>
#include <cmath>
#include <time.h>
#include <sstream>
#include <fstream>
#include <map>

// https://github.com/lava/matplotlib-cpp used for plotting the data
// requires python interpreter to be included and linked within compiler arguments
// If using vscode, vcpkg has a package for easier installation
#include "matplotlibcpp.h"


// struct for the each of the points
struct Point {

    // cords of the point
    // for now, I am using the distance of each rider to calculate k-means, but we can easily change this to something else
    double x;
    double y;

    double ridership;          // Number of riders at that station

    Point(double x_inp, double y_inp, int riders) : x(x_inp), y(y_inp), ridership(riders) {};
};

// Used to calculate the centroid of a specific cluster
Point calcCentroid(const std::vector<Point>& cluster) {

    double sumx = 0.0;
    double sumy = 0.0;
    double riders = 0.0;
    for (const Point& p : cluster) { // Take each point in the cluster and add up their x, y positions and the number of riders
        sumx += p.x;
        sumy += p.y;
        riders += p.ridership;
    }
    // Take the sums and divide by the total number of points
    return Point(sumx / cluster.size(), sumy / cluster.size(), riders / cluster.size());

}

// Determine the distance between two points
double dist(const Point& point1, const Point& point2) {

    // Removed the rider_res variable and calculation here. The distance and normal ridership makes for a much more interesting cluster
    double pos_res;
    pos_res = pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2);

    return sqrt(pos_res);
}

// A lot of "Inspiration" came from the K-means wikipedia article, psuedo-code and more technical aspects explained there made this
// much easier to impliment.

// k will represent the number of clusters
std::vector<Point> k_means_cluster(const std::vector<Point>& points, int k, std::vector<int>& clusters) {

    // Randomly choose initital centroids k
    // used the example from the cplusplus.com rand function page
    srand(std::time_t(NULL));              // initialize random seed

    //srand(42); // static seed for debugging

    // Initialize a vector of centroids
    std::vector<Point> centroids;

    for (int i = 0; i < k; ++i) {
        int random = rand() % points.size(); // Choose a centroid at random
        centroids.push_back(points[random]);
    }

    clusters.resize(points.size()); // Ensure that the clusters vector is the correct size
    // Loop until no points change cluster
    bool converged = false;
    while (!converged) {
        converged = true;

        for (int i = 0; i < points.size(); ++i) {
            int near_cent = 0;
            double minimum = std::numeric_limits<double>::max();

            // Assign each point to the "closest" centroid
            for (int j = 0; j < centroids.size(); ++j) {

                double distance = dist(points[i], centroids[j]);

                // If there is another closer centroid
                if (distance < minimum) {
                    minimum = distance; // new closest
                    near_cent = j;      // new closest centroid
                }
            }

            // If a point was assigned to a cluster that was not previously assigned to it, store it and converged is still true
            if (clusters[i] != near_cent) {
                clusters[i] = near_cent;
                converged = false;
            }
            //std::cout << "Point (" << points[i].x << ", " << points[i].y << ") assigned to cluster: " << near_cent << std::endl;

        }
        // Calculate new centroids
        // (the standard implementation uses the mean of all points in a
        // cluster to determine the new centroid)

        for (int i = 0; i < centroids.size(); ++i) {

            std::vector<Point> c_Points;    // cluster containing the points
            for (int j = 0; j < points.size(); ++j) {   // the points within the cluser
                if (clusters[j] == i) {  // Check if point "i" is in cluster "j"
                    c_Points.push_back(points[j]); // push point into the cluster
                }
            }
            if (!c_Points.empty()) {
                centroids[i] = calcCentroid(c_Points);
            }
        }
    }
    return centroids;
}

// Taken from https://stackoverflow.com/questions/48085842/how-do-i-parse-a-csv-with-commas-embedded-in-quoted-fields
// I used this because I am too dumb to realize what double quotes are
std::vector<std::string> csvParser(std::istream& str, std::vector<std::string>& result) {

    std::vector<std::vector<std::string>> lines;
    std::string line;

    if (str) {
        
        while (std::getline(str, line)) {
            size_t n = lines.size();
            lines.resize(n + 1);

            std::istringstream ss(line);
            std::string field, push_field("");
            bool no_quotes = true;

            while (std::getline(ss, field, ',')) {
                if (static_cast<size_t>(std::count(field.begin(), field.end(), '"')) % 2 != 0) {
                    no_quotes = !no_quotes;
                }

                push_field += field + (no_quotes ? "" : ",");

                if (no_quotes) {
                    lines[n].push_back(push_field);
                    push_field.clear();
                }
            }
        }
    }

    for (auto line : lines) {
        for (auto field : line) {
            result.push_back(field);
        }
    }
    return result;
}

int main() {
    // Open the sample data
    std::ifstream file;
    file.open("../data/samples/mta_subway_sample.csv");

    // Get rid of the header on the CSV
    std::string line;
    std::getline(file, line);

    // Create a vector of strings and pass it to the csvParser
    std::vector<std::string> results;
    csvParser(file, results);
    std::string lat, lon, rider;

    // Vector that will be passed to the kMeans function
    std::vector<Point> points;

    // Use the data from the columns that we care about
    // Column 8: ridership
    // Column 10: lat
    // Column 11: long
    int count = 1;
    for (auto& element : results) {
        if (count == 8) {
            rider = element;
        }
        else if (count == 10) {
            lat = element;
        }
        else if (count == 11) {
            lon = element;
        }
        if (count >= 11) {
            points.push_back(Point(stod(lat), stod(lon), stoi(rider)));
            count = -1;
        }
        count += 1;
    }
    int k = 4; // Number of clusters
    std::vector<double> x, y, riders;
    std::vector<int> clust; // Used to display different colors for each cluster
    std::vector<Point> centroids = k_means_cluster(points, k, clust);

    std::vector<std::vector<double>> cluster_x(k), cluster_y(k); // Store the x and y data into vectors with respect to each cluster
    std::vector<double> x_centroids, y_centroids;

    //std::cout << "X: " << iter.x << " Y: " << iter.y << " Ridership: " << iter.ridership << std::endl;

    // Map of colors to distinguish which point belongs to which cluster
    std::map<int, std::string> colors;
    colors[0] = "ob";
    colors[1] = "og";
    colors[2] = "or";
    colors[3] = "oc";
    colors[4] = "om";
    colors[5] = "oy";
    colors[6] = "ok";

    // Loop through the points and add them to a vector in order to plot them
    for (int i = 0; i < points.size(); ++i) { 
        cluster_x[clust[i]].push_back(points[i].x);
        cluster_y[clust[i]].push_back(points[i].y);
    }

    // Loop through the clusters and push them into a vector
    for (int i = 0; i < centroids.size(); ++i) { 
        x_centroids.push_back(centroids[i].x); 
        y_centroids.push_back(centroids[i].y);
    }

    // Plot each of the points and ensure that points of the same cluster are color coordinated
    for (int i = 0; i < k; ++i) {
        matplotlibcpp::plot(cluster_x[i], cluster_y[i], colors[i]);
    }

    // Plot the centroids. They will be marked as a black X
    matplotlibcpp::scatter(x_centroids, y_centroids, 100.0, {{"color", "k"}, {"marker", "x"}});

    // Titles of axis and graph
    matplotlibcpp::xlabel("Longitude");
    matplotlibcpp::ylabel("Lattitude");
    matplotlibcpp::title("K-means clustering based on distance and ridership");
    matplotlibcpp::show();
    
    return 0;
}
