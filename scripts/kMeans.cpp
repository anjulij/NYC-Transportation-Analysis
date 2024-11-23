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
#include <algorithm>
//#include <direct.h>


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

    double pos_res, rider_res;
    pos_res = pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2);

    rider_res = pow(point1.ridership - point2.ridership, 2);

    return sqrt(pos_res + rider_res);
}

// A lot of "Inspiration" came from the K-means wikipedia article, psuedo-code and more technical aspects explained there made this
// much easier to impliment.

// k will represent the number of clusters
std::vector<Point> k_means_cluster(const std::vector<Point>& points, int k) {

    // Randomly choose initital centroids k
    // used the example from the cplusplus.com rand function page
    srand(time(NULL));              // initialize random seed

    //srand(42); // static seed for debugging

    // Initialize a vector of centroids
    std::vector<Point> centroids;

    for (int i = 0; i < k; ++i) {
        int random = rand() % points.size(); // Choose a centroid at random
        centroids.push_back(points[random]);
    }
    // Vector that will track the points and their respective clusters
    std::vector<int> clusters(points.size(), -1);

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
            //std::cout << "Point (" << points[i].x << ", " << points[i].y << ") assigned to cluster " << near_cent << std::endl;
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

    // Print out the data of the columns we care about
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
    auto test = k_means_cluster(points, 2);
 
    for (auto iter : test) {
       std::cout << "X: " << iter.x << " Y: " << iter.y << " Ridership: " << iter.ridership << std::endl;
    }

    return 0;
}
